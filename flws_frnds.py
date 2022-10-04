
# import libraries and important functions from keys_utils file
import random
from keys_utils import api_mac, api_noise, api_x, never_twice, write_to_file, clear_file

# define the .txt files used for the various lists of accounts 
FLW_LIST = 'files/followers.txt'
BIG_LIST = 'files/big_accounts.txt'
USED = 'files/used_accs.txt'



#===============================================================================================
#================================== ACCOUNTS FUNCTIONS =========================================
#===============================================================================================



# goes trough all of my followers and stores their informations
def store_flwrs_info(FILE):
    # get the ids of my followers
    my_followers = api_mac.get_follower_ids()
    i = 0
    for follower in my_followers:
        # get the user's info packet
        flw_data = api_mac.get_user(user_id = follower)
        follower_id = flw_data.id_str
        # get their screen name 
        follower_name = flw_data.screen_name
        # get the number of followers they have
        flw_flw = flw_data.followers_count
        useful_data = str(follower_id + '-' + follower_name + '-' + str(flw_flw))
        # write them in the file specified in the function argument
        write_to_file(FILE, useful_data)
        i+=1
    # log the console with how many followers info were stored    
    print(str(i)+ " followers info stored")
    
    
    
# update all of the informations about my followers
def update_flwrs_info(FILE):
    # clear blank the file from the argument
    clear_file(FILE)
    # call the storing function created up here for the same file
    store_flwrs_info(FILE)
  
  
  
def store_big_accs(FILE, account_limit):
    # defining a variable for how many accounts will be stored
    stored = 0
    # open the file specified in the function argument
    with open(FILE, 'r') as file:
        # read it line by line, every line is a twttr profile
        accounts = file.readlines()
        for account in accounts:
            # get the number of followers for the profile
            account_followers = account.split('-')[2]
            # if they have more followers than specified in the function second argument
            if int(account_followers) > account_limit:
                # write the info in the BIG_LIST txt file
                write_to_file(BIG_LIST, account.strip())
                # augment the stored variable by one
                stored +=1
            else: pass
    # console log the numbers of accounts stored 
    # or tell me if there were no accounts big enough to be stored
    if stored > 0:
        print("I've stored "+str(stored)+" accounts.")
    else: print("No big accounts to store")
 
 
 
# function to take one random account from a specified list
def rand_acc(FILE):
    # open the specified file
    file = open(FILE, 'r')
    # read it line by line
    lines = file.readlines()
    # use the never_twice function taken from keys_utils.py
    # to avoid calling the same random lines over and over
    chance = never_twice(lines, USED)
    # split the string to get the id and the return it 
    id  = lines[chance].split('-')[0]
    return id
                   
                   
                   
# call to get one random follower from one random account        
def rand_flwr_rand_acc(FILE):
    # using the rand_acc function above on the file specified in the function argument
    rand_acc_id  = rand_acc(FILE)
    # get the ids of the first ten followers of that account
    acc_flwrs = api_mac.get_follower_ids(user_id= rand_acc_id, count = 10)
    # choose one random id from the list the api just gave us
    bound = len(acc_flwrs)
    chance = random.randrange(bound-1)
    # then return that id just chosen
    rand_acc_flwr_id = acc_flwrs[chance]
    return rand_acc_flwr_id



# call to get one random friendtw from one random account        
def rand_frnd_rand_acc(FILE):
    # using the rand_acc function above on the file specified in the function argument
    rand_acc_id  = rand_acc(FILE)
    # get the ids of the first ten followers of that account
    acc_frnds = api_mac.get_friend_ids(user_id= rand_acc_id, count = 10)
    # choose one random id from the list the api just gave us
    bound = len(acc_frnds)
    chance = random.randrange(bound-1)
    # then return that id just chosen
    rand_acc_frnd_id = acc_frnds[chance]
    return rand_acc_frnd_id
     
     
     
#================================ GET USER TIMELINE TWEETS =====================================
#===============================================================================================

def timeline(_id, how_many):
    # empy array to fill with tweets texts
    twts = []
    # empty array to fill with the ids of those tweets
    twts_ids = []
    # call the api for an -how_many- number of all the tweets in the timeline 
    # of the user id specified in the first argument
    all_the_tweets = api_mac.user_timeline(user_id = _id, count = how_many, exclude_replies=True)
    # for every objct in the api reply spli the text and the id
    # and add them to the arrays created up here
    for tweet in all_the_tweets:
        twts.append(tweet.text)
        twts_ids.append(tweet.id_str)
    # return the arrays with all the infos
    return twts, twts_ids

def handle_timeline(my_usr, screen_name, how_many):
    if(my_usr == "mac"): api = api_mac
    if(my_usr == "x"): api = api_x
    if(my_usr == "noise"): api = api_noise
    # empy array to fill with tweets texts
    twts = []
    # empty array to fill with the ids of those tweets
    twts_ids = []
    # empty array to fill with tweets objects
    twts_obj = []
    # call the api for an -how_many- number of all the tweets in the timeline 
    # of the user id specified in the first argument
    all_the_tweets = api.user_timeline(screen_name = screen_name, count = how_many, exclude_replies=True, include_rts=False)
    # for every objct in the api reply spli the text and the id
    # and add them to the arrays created up here
    for tweet in all_the_tweets:
        twts.append(tweet.text)
        twts_ids.append(tweet.id_str)
        twts_obj.append(tweet)
    # return the arrays with all the infos
    return twts, twts_ids, twts_obj


# update_flwrs_info(FLW_LIST)
# rand_frnd_rand_acc(BIG_LIST)
