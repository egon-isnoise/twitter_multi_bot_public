# import libraries
import tweepy 
import random


#================================ API KEYS FOR Mac Shiller =====================================
#===============================================================================================
#====================================== NFT Shiller ============================================

consumer_key_mac = ''
consumer_secret_mac = ''
access_token_mac = ''
access_token_secret_mac = ''

auth_mac = tweepy.OAuthHandler(consumer_key_mac, consumer_secret_mac)
auth_mac.set_access_token(access_token_mac, access_token_secret_mac)
api_mac = tweepy.API(auth_mac, wait_on_rate_limit = True)  


#============================ API KEYS FOR egonisnoise.eth =====================================
#===============================================================================================
#==================================== IamNoise3 APP ============================================

consumer_key_noise = ''
consumer_secret_noise = ''
access_token_noise = ''
access_token_secret_noise = ''

auth_noise = tweepy.OAuthHandler(consumer_key_noise, consumer_secret_noise)
auth_noise.set_access_token(access_token_noise, access_token_secret_noise)
api_noise = tweepy.API(auth_noise, wait_on_rate_limit = True)  


#================================ API KEYS FOR Xefler =====================================
#===============================================================================================
#====================================== NFT Shiller ============================================

consumer_key_x = ''
consumer_secret_x = ''
access_token_x = ''
access_token_secret_x = ''

auth_x = tweepy.OAuthHandler(consumer_key_x, consumer_secret_x)
auth_x.set_access_token(access_token_x, access_token_secret_x)
api_x = tweepy.API(auth_x, wait_on_rate_limit = True)  


#===============================================================================================
#============================= WRITE/DELETE DATA FUNCTIONS =====================================
#===============================================================================================


# writing information to a file in one single function
def write_to_file(FILE, info):
    file_write = open(FILE, 'a')
    file_write.write(str(info) + '\n')
    file_write.close()
    return
     
     
# clearing the file to a blank slate in a single fucntion
def clear_file(FILE):
    with open(FILE, "w"):
        pass
    
#=============================== AVOIDING SPAMMY BEHAVIOUR =====================================
#===============================================================================================

# always get a different random output
def never_twice(list, FILE):
    # try get a random number for the length of the list in the argument
    chance = random.randrange(len(list)-1)
    # open the file from the second argument and read it line by line
    file_read = open(FILE, 'r')
    lines = file_read.readlines()
    # if the length of list and FILE is the same it means 
    # we used all the possible random numbers so wipe clean FILE
    if len(lines) == len(list)-1: clear_file(FILE) 
    else:
        # if the "chance" created is already present, create a new chance
        while str(chance)+'\n' in lines:
            chance = random.randrange(len(list)-1)
    # when is not write it to the file
    write_to_file(FILE, chance)
    # return the chance created
    return chance

def no_spam(FILE):
    file_read = open(FILE, 'r')
    id = file_read.readlines()
    return id

# wtf = api.rate_limit_status(resources = 'favorites')
# print(wtf)
