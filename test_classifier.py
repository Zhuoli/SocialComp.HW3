'''
Created on Nov 12, 2013

@author: Qizhen Ruan
'''
import os
from classify import Classifier
from stop_words import STOP_WORDS

def get_dir_and_labels(corpus='corpus'):
    cur_dir = os.path.dirname(__file__)
    spam_dir = os.path.join(cur_dir, corpus, 'spam')
    ham_dir = os.path.join(cur_dir, corpus, 'ham')
    return (spam_dir, 'spam'), (ham_dir, 'ham')

def get_file_list(path, selector=None):
    files = os.listdir(path)
    if selector:
        files = [f for i, f in enumerate(sorted(files)) if selector(i)]
    return files

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

        
if __name__ == '__main__':
    classifier = Classifier.load('classifier.bin')
    for d, l in get_dir_and_labels():
        test_enron_files(classifier, d, l)