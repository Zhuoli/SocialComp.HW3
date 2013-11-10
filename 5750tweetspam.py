#!/usr/bin/env python
'''
connect to Twitter and output user IDs that will be banned
Created on Oct 29, 2013  @Qizhen
'''
import time
import crawler
import recorder
import settings


def main():
    while True:
        try:
            # crawl twitter accounts
            twitter_crawler = crawler.CrawlerThread()
            twitter_crawler.start()
            
            # check and print out spam
            twitter_recorder = recorder.RecorderThread()
            twitter_recorder.start()
            
            twitter_crawler.join()
        except:
            if settings.DEBUG:
                print '**************** exception, restart ******************************' 
                    
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
