'''
Created on Feb 16, 2015

@author: goris
'''

import httplib
import urllib
import datetime, time
import json

class TweetCollector(object):
    
    host = 'api.topsy.com'
    url = '/v2/content/tweets.json'
    API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
    hashtags = ['#SuperBowlXLIX','#Seahawks','#Patriots','#GoHawks','#GoPatriots','#Halftime','#superbowlcommercials']
    start_date = datetime.datetime(2015,01,14, 12,30,0)
    end_date = datetime.datetime(2015,01,29, 17,15,0)
    mintime = int(time.mktime(start_date.timetuple()))
    maxtime = int(time.mktime(end_date.timetuple()))
    filesPath = '/Users/goris/Desktop/tweets/'

   # def __init__(self):
        
    def getTweets(self):
        for hashtag in self.hashtags:
            params = urllib.urlencode({'apikey' : self.API_KEY, 'q' :hashtag,
                           'mintime': str(self.mintime), 'maxtime': str(self.maxtime),
                           'new_only': '1', 'include_metrics':'1', 'limit': 20})
            
            req_url = self.url + '?' + params
            req = httplib.HTTPConnection(self.host)
            req.putrequest("GET", req_url)
            req.putheader("Host", self.host)
            req.endheaders()
            req.send('')
            resp = req.getresponse()
            print resp.status, resp.reason
            resp_content = resp.read()
            ret = json.loads(resp_content)
            tweets = ret['response']['results']['list']
            print tweets
            print "----------------------"
            filePath = self.filesPath + hashtag + ".txt"
            with open(filePath, 'wr') as file:
                file.write(tweets.__str__())
                file.close()
        print "##########################"