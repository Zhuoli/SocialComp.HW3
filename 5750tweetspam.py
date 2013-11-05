#!/usr/bin/env python
'''
connect to Twitter and output user IDs that will be banned
Created on Oct 29, 2013  @Qizhen
'''
import time
import crawler
import recorder


def main():
    while True:
        try:
            twitter_crawler = crawler.CrawlerThread()
            twitter_crawler.start()
            
            twitter_recorder = recorder.RecorderThread()
            twitter_recorder.start()
            
            twitter_crawler.join()
        except:
            try:
                twitter_crawler.stop()
            except:
                pass
            
            try:
                twitter_recorder.stop()
            except:
                pass
            
            time.sleep(600)

if __name__ == "__main__":
    main()
