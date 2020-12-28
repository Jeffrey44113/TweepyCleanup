import tweepy
import json
import csv

from config import create_api

api = create_api()

#get every tweet in timeline 
for tweety in tweepy.Cursor(api.user_timeline).items():
    try:
        api.destroy_status(tweety.id)
        print("Deleted:", tweety.text.encode("utf-8"))
    except:
        print("Failed to remove!: ", tweety.id)
