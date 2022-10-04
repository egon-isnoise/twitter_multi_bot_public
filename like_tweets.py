
# import libraries and functions from the other files
from distro import like
from numpy import NaN
from pyparsing import line
from distutils.log import error
from keys_utils import api_mac, api_noise, api_x, never_twice
from flws_frnds import timeline
import random
import tweepy

# define costant files

LAST_LIKED_TWEET = 'files/last_seen_reply.txt'


#================================= LIKE STUFF FUNCTIONS =====================================
#===============================================================================================
 
# function to like one random tweet from some accounts
def like_rand_tweet(usr, user_id, how_many):
    if(usr == "mac"): api = api_mac
    if(usr == "x"): api = api_x
    if(usr == "noise"): api = api_noise

    # gets an array of tweets from that account
    possible_fave = timeline(user_id, how_many)
    # chooses one randomly and saves its id
    chance = random.randrange(len(possible_fave[1])-1) 
    fave_id = possible_fave[1][chance]
    # if there actually is one
    if(chance != NaN): 
        fave_id = possible_fave[1][chance]
        # like it and console logs which one it liked
        try:
            api.create_favorite(id= fave_id)
            print('I liked the tweet with ID: '+ fave_id +'\n')
        # tells me possible errors
        except tweepy.errors.HTTPException as e: 
            print('==================================================')
            print(e)
            print('==================================================')  
    # if there are no tweets in specified range it tells me in the console
    else:
        print("No tweet to like")
  

# like an NFT reply to your tweet and like a random tweet from that user
def like_replies_and_rndm_tweet(usr):
    if(usr == "mac"): api = api_mac
    if(usr == "x"): api = api_x
    if(usr == "noise"): api = api_noise
    #  check tweets mentions, this is a method where you HAVE TO specify what argument is what 
    tweets = api.mentions_timeline(count=10, tweet_mode = 'extended')

    # check if they contain a specific word/phrase/hashtag
    for tweet in reversed(tweets):   
        fave_id = str(tweet.id) 
        user = tweet.user.screen_name
        user_id = tweet.user.id
        try:
            # like the tweet
            api.create_favorite(fave_id)
            print('I liked the reply to my tweet with ID: '+ fave_id+'\n')
            # # print the user handle(?)
            print('From the user ' +user +'\n')
            like_rand_tweet(usr, user_id, 5)
        except tweepy.errors.HTTPException as e: 
            print('==================================================')
            print(e)
            print('==================================================')  
    # if there are no tweets in specified range it tells me in the console
    else:
        print("No more replies and random tweets to like")

   

# like_replies_and_rndm_tweet("mac")

