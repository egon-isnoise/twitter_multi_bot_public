
from keys_utils import api_mac, api_noise, api_x
import tweepy

# separate old tweets from new ones by saving IDs in a file
LAST_LIKED_EGON = 'files/egon_last_liked.txt'
LAST_LIKED_XEFLER = 'files/xefler_last_liked.txt'
LAST_LIKED_MAC = 'files/mac_last_liked.txt'

# read the id of the last seen tweet in the .txt file
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

# store the id of the last seen tweet in the .txt file
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

#get the timelines of my accounts
def timelineMac(usr):
    # empy array to fill with tweets texts
    twts = []
    # empty array to fill with the ids of those tweets
    twts_ids = []
    # call the api for an -how_many- number of all the tweets in the timeline 
    # of the user id specified in the first argument
    if(usr == "noise"): api = api_noise
    if(usr == "x"): api = api_x
    all_the_tweets = api.user_timeline(screen_name= "shiller_mac", count = 5, exclude_replies="true", include_rts= "false")
    # for every objct in the api reply spli the text and the id
    # and add them to the arrays created up here
    for tweet in all_the_tweets:
        twts.append(tweet)
        twts_ids.append(tweet.id_str)
    # return the arrays with all the infos
    # print(twts, twts_ids)
    return twts, twts_ids

def timelineEgon(usr):
    # empy array to fill with tweets texts
    twts = []
    # empty array to fill with the ids of those tweets
    twts_ids = []
    # call the api for an -how_many- number of all the tweets in the timeline 
    # of the user id specified in the first argument
    if(usr == "mac"): api = api_mac
    if(usr == "x"): api = api_x
    all_the_tweets = api.user_timeline(screen_name= "egonisnoise", count = 5, exclude_replies="true", include_rts= "false")
    # for every objct in the api reply spli the text and the id
    # and add them to the arrays created up here
    for tweet in all_the_tweets:
        twts.append(tweet)
        twts_ids.append(tweet.id_str)
    # return the arrays with all the infos
    # print(twts, twts_ids)
    return twts, twts_ids

def timelineXefler(usr):
    # empy array to fill with tweets texts
    twts = []
    # empty array to fill with the ids of those tweets
    twts_ids = []
    # call the api for an -how_many- number of all the tweets in the timeline 
    # of the user id specified in the first argument
    if(usr == "mac"): api = api_mac
    if(usr == "noise"): api = api_noise
    all_the_tweets = api.user_timeline(screen_name= "Xefler2022", count = 5, exclude_replies="true", include_rts= "false")
    # for every objct in the api reply spli the text and the id
    # and add them to the arrays created up here
    for tweet in all_the_tweets:
        twts.append(tweet)
        twts_ids.append(tweet.id_str)
    # return the arrays with all the infos
    # print(twts, twts_ids)
    return twts, twts_ids


# like tweets from my accounts
def like_mac_last_tweets(usr):
    if(usr == "noise"): api = api_noise
    if(usr == "x"): api = api_x
    last_tweets_ids = timelineMac(usr)[1]
    last_tweets_obj = timelineMac(usr)[0]
    for tweet_id in last_tweets_ids:
        # print(tweet_id)
        try:
            api.create_favorite(id= tweet_id)
            print('== '  +usr+' == liked the tweet with ID: '+ tweet_id +' on MAC\' s timeline\n')
        # tells me possible errors
        except tweepy.errors.HTTPException as e: 
            print('==================================================')
            print(e)
            print('==================================================')
    for tweet in last_tweets_obj:
        # print(tweet_id)
        if("https://" in tweet.text): 
            try:
                api.retweet(id= tweet.id_str)
                print('== '  +usr+' == retweeted the tweet with ID: '+ tweet.id_str +' on MAC\' s timeline\n')
            # tells me possible errors
            except tweepy.errors.HTTPException as e: 
                print('==================================================')
                print(e)
                print('==================================================')  
    # if there are no tweets in specified range it tells me in the console
    else:
        print("No tweet to rt")

    
def like_egon_last_tweets(usr):
    if(usr == "mac"): api = api_mac
    if(usr == "x"): api = api_x
    last_tweets_ids = timelineEgon(usr)[1]
    last_tweets_obj = timelineEgon(usr)[0]
    for tweet_id in last_tweets_ids:
        # print(tweet_id)
        try:
            api.create_favorite(id= tweet_id)
            print('== '  +usr+' == liked the tweet with ID: '+ tweet_id +' on EGONISNOISE\' s timeline\n')
        # tells me possible errors
        except tweepy.errors.HTTPException as e: 
            print('==================================================')
            print(e)
            print('==================================================')  
    for tweet in last_tweets_obj:
        # print(tweet_id)
        if("https://" in tweet.text): 
            try:
                api.retweet(id= tweet.id_str)
                print('== '  +usr+' == retweeted the tweet with ID: '+ tweet.id_str +' on MAC\' s timeline\n')
            # tells me possible errors
            except tweepy.errors.HTTPException as e: 
                print('==================================================')
                print(e)
                print('==================================================') 
    # if there are no tweets in specified range it tells me in the console
    else:
        print("No tweet to rt")


def like_xefler_last_tweets(usr):
    if(usr == "mac"): api = api_mac
    if(usr == "noise"): api = api_noise
    last_tweets_ids = timelineXefler(usr)[1]
    last_tweets_obj = timelineXefler(usr)[0]
    for tweet_id in last_tweets_ids:
        try:
            api.create_favorite(id= tweet_id)
            print('== ' +usr+' == liked the tweet with ID: '+ tweet_id +' on XEFLER\' s timeline\n')
        # tells me possible errors
        except tweepy.errors.HTTPException as e: 
            print('==================================================')
            print(e)
            print('==================================================')  
        print("No tweet to like") 
    for tweet in last_tweets_obj:
        # print(tweet_id)
        if("https://" in tweet.text): 
            try:
                api.retweet(id= tweet.id_str)
                print('== '  +usr+' == retweeted the tweet with ID: '+ tweet.id_str +' on MAC\' s timeline\n')
            # tells me possible errors
            except tweepy.errors.HTTPException as e: 
                print('==================================================')
                print(e)
                print('==================================================') 
    # if there are no tweets in specified range it tells me in the console
    else:
        print("No tweet to rt")



# like_mac_last_tweets("noise")