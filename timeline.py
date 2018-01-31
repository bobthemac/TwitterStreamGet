#!/usr/bin/env python

from __future__ import print_function

import argparse
import time

import twitter

TWITTER_CONSUMER_KEY = 'consumer_key'
TWITTER_CONSUMER_SECRET = 'consumer_secret'
TWITTER_ACCESS_TOKEN_KEY =  'access_token'
TWITTER_ACCESS_TOKEN_SECRET = 'access_token_secret'

api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY, consumer_secret=TWITTER_CONSUMER_SECRET, access_token_key=TWITTER_ACCESS_TOKEN_KEY, access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

fpath = 'f1-sample-live.txt'

max_id = None
with open(fpath, 'ab') as f:
	for tweets in api.GetStreamFilter(track=["f1", "F1", "FORUMULA ONE", "FORUMULA 1"]):
		if tweets.has_key('text'):
			try:
				if len(tweets['text']) > 1:
					print(tweets['text'], file=f)
			except:
				continue
