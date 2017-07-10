#!/bin/python

import praw
import sys

#enter username here
username = ''

#generate an api key here:https://www.reddit.com/prefs/apps/, use script and random redirect uri. 
reddit = praw.Reddit(user_agent='Karma fetcher by /u/you',client_id='',client_secret='',password='',username=username)

user = reddit.redditor(username)

#uncomment line below to display username in bar
#sys.stdout.write(str(user)),sys.stdout.write(': ')
sys.stdout.write(str(user.link_karma) + ' - ' + str(user.comment_karma))
