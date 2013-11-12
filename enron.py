import optparse
import sys
import os

from classify import Classifier
from stop_words import STOP_WORDS


def load_classifier():
    if not os.path.exists('classifier.db'):
        sys.stderr.write('Unable to load classifier.db -- please run this script first')
        sys.exit(1)
    return Classifier.load('classifier.db')

def extract_words(s, min_len=2, max_len=20):
    """
    Extract all the words in the string ``s`` that have a length within
    the specified bounds and which are not known stop words
    """
    words = []
    for w in s.lower().split():
        wlen = len(w)
        if w not in STOP_WORDS and wlen > min_len and wlen < max_len:
            words.append(w)
    return words

def email_extract(subject, body, min_len=2, max_len=20):
    """
    Handle a subject and body and extract the features correctly
    """
    terms = ['s:%s' % w for w in extract_words(subject, min_len, max_len)]
    terms.extend(extract_words(body, min_len, max_len))
    return terms

def enron_email_extract(text, min_len=2, max_len=20):
    """
    Enron email messages contain a subject line followed by content, so adapt
    the feature extraction to properly parse out the subject line and body
    """
    lines = []
    subj = ''
    for line in text.splitlines():
        if line.startswith('subject:'):
            is_subj = True
            subj = line[8:]
        else:
            lines.append(line)
    return email_extract(subj, ' '.join(lines), min_len, max_len)

def get_file_list(path, selector=None):
    files = os.listdir(path)
    if selector:
        files = [f for i, f in enumerate(sorted(files)) if selector(i)]
    return files

def get_dir_and_labels(corpus='corpus'):
    cur_dir = os.path.dirname(__file__)
    spam_dir = os.path.join(cur_dir, corpus, 'spam')
    ham_dir = os.path.join(cur_dir, corpus, 'ham')
    return (spam_dir, 'spam'), (ham_dir, 'ham')

def train_enron_files(classifier, path, label, selector=None):
    files = get_file_list(path, selector)
    file_count = len(files)
    ten_pct = file_count / 10.0
    vals = dict((int(j * ten_pct), '%s%%' % (j * 10)) for j in range(1, 11))
    for i, filename in enumerate(files):
        with open(os.path.join(path, filename)) as fh:
            contents = fh.read()
        features = enron_email_extract(contents)
        if i in vals:
            print vals[i]
        classifier.train(features, [label])
    print 'Done with %s -- trained %s documents' % (label, file_count)

def train_all(selector, corpus):
    classifier = Classifier()
    for d, l in get_dir_and_labels(corpus):
        train_enron_files(classifier, d, l, selector)
    return classifier

def test_enron_files(classifier, path, label, selector=None):
    files = get_file_list(path, selector)
    correct = total = 0
    for filename in files:
        with open(os.path.join(path, filename)) as fh:
            contents = fh.read()
        features = enron_email_extract(contents)
        res = classifier.classify(features)
        best = res[0][0]
        if best == label:
            correct += 1
        total += 1
    pct = 100 * (float(correct) / total)
    print 'Accuracy of "%s": %s%% based on %s documents' % (label, pct, total)

def test_all(selector, corpus):
    classifier = load_classifier()
    for d, l in get_dir_and_labels(corpus):
        test_enron_files(classifier, d, l, selector)

def download_extract():
    import tarfile
    import urllib
    url = 'http://media.charlesleifer.com/downloads/misc/corpuses.tar.gz'
    print 'Downloading %s' % url
    urllib.urlretrieve(url, 'corpuses.tar.gz')
    print 'successfully downloaded...extracting...'
    archive = tarfile.open('corpuses.tar.gz', 'r:gz')
    archive.extractall(os.path.dirname(__file__) or '.')
    print 'successfully extracted'

def make_selector(p):
    def train(i):
        return i % 100 <= p
    def test(i):
        return i % 100 > p
    return train, test

def get_option_parser():
    parser = optparse.OptionParser()
    parser.add_option('-d', '--download', action='store_true', help='download corpuses')
    parser.add_option('-l', '--load', action='store_true', help='re-load the database')
    parser.add_option('-t', '--test', action='store_true', help='test accuracy')
    parser.add_option('-r', '--refresh', action='store_true', help='re-load the database and run tests')
    parser.add_option('-p', '--percent', type='int', help='percent of data to use for training, remainder for testing')
    parser.add_option('-c', '--corpus', help='corpus to use (defaults to "corpus")')
    return parser

if __name__ == '__main__':
    parser = get_option_parser()
    options, args = parser.parse_args()
    if options.download or (
            not os.path.exists(os.path.join(os.path.dirname(__file__), 'corpus')) and \
            raw_input('Corpus not found - download now? [Yn] ') != 'n'):
        download_extract()
    if options.percent:
        if options.percent < 1 or options.percent > 99:
            sys.stderr.write('Invalid percent, must be between 1 and 99')
            sys.exit(1)
        print 'Using %s - %s train/test' % (options.percent, 100 - options.percent)
        s_train, s_test = make_selector(options.percent)
    else:
        s_train = s_test = None
    corpus = options.corpus or 'corpus'
    if options.load or options.refresh:
        classifier = train_all(s_train, corpus)
        classifier.save('classifier.db')
    if options.test or options.refresh:
        test_all(s_test, corpus)