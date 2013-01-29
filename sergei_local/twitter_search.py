#! /usr/bin/python
# twitter_search.py
# Author: Pete Milne
# Date: 28-01-2013
# Version: 1.0
# Twitter API search for hashtag
# Usage: python twitter_search.py <'#hashtag'>


import sys
from twitter import *

HASHTAG = sys.argv[1]

# Instansiate Twitter object
twitter_search = Twitter(domain="search.twitter.com")

# Search for hashtag - equivalent to 
# http://search.twitter.com/search.json?q=%23sergeithemeerkat
# query = twitter_search.search(q="#sergeithemeerkat")
query = twitter_search.search(q=HASHTAG)

# loop through json result
last_result = "Mon, 28 Jan 2013 22:20:28 +0000"
for result in query["results"]:
	if result["created_at"] >= last_result:
		print ("(%s) @%s %s" % (result["created_at"], result["from_user"], result["text"]))
		last_result = result["created_at"]
