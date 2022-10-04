# import libraries
import asyncio
import random
import time
from post import tweet_art, drop_me_NFTs
from like_my_accounts import like_egon_last_tweets, like_xefler_last_tweets, like_mac_last_tweets
from like_tweets import like_replies_and_rndm_tweet
from rt_specified import retweet_my_own_shills, delete_my_own_shills,retweet_from_my_favourites


#========================= TELL THE TIME LOL in a very philosophical function
def what_is_time():
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    print('Action performed at time: ' + curr_time)

#===============================================================================================
#=============================== ASYNC POST/LIKE FUNCTIONS =====================================
#===============================================================================================

# asynchronous function that checks and likes some specified users' tweets every hour (in rotation)
async def specific_likes_every_hour_plus():
    # waiting 10 minutes to start the routine
    await asyncio.sleep(600)
    # console log stuff
    while True:
        try:
            print('========== LIKE MAC LAST TWEETS... ==========')
            # like last MAC tweets
            like_mac_last_tweets("x")
            what_is_time()
            # sleep 5
            await asyncio.sleep(300)
            like_mac_last_tweets("noise")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700)) 
            print('========== LIKE EGON LAST TWEETS... ==========')
            # like egon last tweets
            like_egon_last_tweets("mac")
            what_is_time()
            # sleep 5
            await asyncio.sleep(300)
            like_egon_last_tweets("x")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700)) 
            print('========== LIKE XEFLER LAST TWEETS... ==========')
            # like Xefler last tweets
            like_xefler_last_tweets("mac")
            what_is_time()
            # sleep 5
            await asyncio.sleep(300)
            like_xefler_last_tweets("noise")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))  
        except Exception:
            print('========== SOME CAME UP WHILE LIKING STATUSES... ==========')
            what_is_time()
            # sleeping for 10/15 minutes
            await asyncio.sleep(random.randint(600, 900))

# fucntion that updates my status asking for a shill every hour
async def shill_me_every_hour():
    # console logging the events
    while True:
        try:
            print('========== UPDATE MAC SHILLS... ==========')
            # calling the drop me NFTs function
            drop_me_NFTs("mac")
            what_is_time()
            # sleeping for 20/25 minutes
            await asyncio.sleep(random.randint(1200, 1500))
            print('========== UPDATE EGON SHILLS... ==========')
            # calling the drop me NFTs function
            drop_me_NFTs("noise")
            what_is_time()
            # sleeping for 20/25 minutes
            await asyncio.sleep(random.randint(1200, 1500))
            print('========== UPDATE XEFLER SHILLS... ==========')
            # calling the drop me NFTs function
            drop_me_NFTs("x")
            what_is_time()
            # sleeping for 20/25 minutes
            await asyncio.sleep(random.randint(1200, 1500))
        except Exception:
                print('========== SOME CAME UP WHILE SHILLING... ==========')
                what_is_time()
                # sleeping for 20/25 minutes
                await asyncio.sleep(random.randint(1200, 1500))
        
# function that tweets some of the art in the folders every 4 hours
async def tweet_art_every_3_hours():
    # waiting 5 minutes to start the routine
    await asyncio.sleep(300)
    # logging all the events
    while True:
        try:
            print('========== UPDATE MAC STATUS... ==========')
            # calling the tweet art function for xefler
            tweet_art("mac", "komiks")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))  
            # calling the tweet art function for egonisnoise
            print('========== UPDATE EGON STATUS... ==========')
            choice = random.randint(1, 3)
            if (choice == 0): collection = "gravite"
            if (choice == 1): collection = "solipsism"
            if (choice == 2): collection = "faoona"
            tweet_art("noise", collection)
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))
            print('========== UPDATE XEFLER STATUS... ==========')  
            tweet_art("x", "reflections")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))  
        except Exception:
            print('========== SOME CAME UP WHILE UPDATING ART... ==========')
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700)) 

# function that retweets some of the art from favorite accounts
async def retweet_art_every_2_hours():
    # logging all the events
    while True:
        try:
            print('========== MAC IS RETWEETING ART... ==========')
            # calling the tweet art function for xefler
            retweet_from_my_favourites("mac")
            what_is_time()
            # sleeping for ~ 45m 
            await asyncio.sleep(random.randint(2700, 3000))  
            # calling the tweet art function for egonisnoise
            print('========== EGON IS RETWEETING ART... ==========')
            retweet_from_my_favourites("noise")
            what_is_time()
            # sleeping for ~ 45m 
            await asyncio.sleep(random.randint(2700, 3000))  
            # print('===================== Retweeting art... =============================')
            # retweet_from_my_favourites("x")
            # what_is_time()
            # # sleeping for ~ 45m 
            # await asyncio.sleep(random.randint(2700, 3000))  
        except Exception:
            print('========== SOME CAME UP WHILE RETWEETING ART... ==========')
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700)) 

# function that checks the replies to shill tweets and likes tweets from those accounts
async def like_replies_every_3():
    # sleeping for 20 minutes
    await asyncio.sleep(1200)
    while True:
        try:
            print('========== LOOKING FOR MAC REPLIES... ==========')
            # calling the like replies function for mac
            like_replies_and_rndm_tweet("mac")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))  
            print('========== LOOKING FOR EGON REPLIES... ==========')
            # calling the like replies function for noise
            like_replies_and_rndm_tweet("noise")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))  
            print('========== LOOKING FOR XEFLER REPLIES... ==========')
            # calling the like replies function for xefler
            like_replies_and_rndm_tweet("x")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))   
        except Exception:
            print('========== SOME CAME UP WHILE LIKING REPLIES... ==========')
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700)) 
    
# function that checks the replies to shill tweets and likes tweets from those accounts
async def rt_shills_every_3():
    # sleeping for ~ 1h 
    await asyncio.sleep(random.randint(3600, 3700))
    while True:
        try:
            print('========== LOOKING FOR XEFLER SHILLS... ==========')
            # calling the like replies function for mac
            retweet_my_own_shills("x")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))  
            print('========== LOOKING FOR EGON SHILLS... ==========')
            # calling the like replies function for noise
            retweet_my_own_shills("noise")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))  
            print('========== LOOKING FOR MAC SHILLS... ==========')
            # calling the like replies function for xefler
            retweet_my_own_shills("mac")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))   
        except Exception:
            print('========== SOME CAME UP WHILE RETWEETING SHILLS... ==========')
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700)) 

 # function that checks the likes to shill and deletes unliked tweets
async def clean_shills_every_3():
    # sleeping for ~ 2h 
    await asyncio.sleep(random.randint(7200, 7400))
    while True:
        try:
            print('========== LOOKING FOR XEFLER SHILLS... ==========')
            # calling the like replies function for mac
            delete_my_own_shills("x")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))  
            print('========== LOOKING FOR EGON SHILLS... ==========')
            # calling the like replies function for noise
            delete_my_own_shills("noise")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))  
            print('========== LOOKING FOR MAC SHILLS... ==========')
            # calling the like replies function for xefler
            delete_my_own_shills("mac")
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700))   
        except Exception:
            print('========== SOME CAME UP WHILE DELETING SHILLS... ==========')
            what_is_time()
            # sleeping for ~ 1h 
            await asyncio.sleep(random.randint(3600, 3700)) 

#===============================================================================================   
#========================== THIS FUNCTION IS THE ACTUAL 'BOT'   
#===============================================================================================


async def be_a_bot():
    task0 = asyncio.create_task(retweet_art_every_2_hours())
    task1 = asyncio.create_task(specific_likes_every_hour_plus())
    task2 = asyncio.create_task(shill_me_every_hour())
    task3 = asyncio.create_task(tweet_art_every_3_hours())
    task4 = asyncio.create_task(like_replies_every_3())
    task5 = asyncio.create_task(rt_shills_every_3())
    task6 = asyncio.create_task(clean_shills_every_3())

    await task0


#========================= HERE WE 'RUN' THE BOT  (gotta call this file with Python3.7 or asyncio does not work)
asyncio.run(be_a_bot())


    


