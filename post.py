
# import libraries and functions from the other files
from distro import like
from numpy import NaN
from pyparsing import line
from distutils.log import error
from keys_utils import api_mac, api_noise, api_x, never_twice
import random
import tweepy
import emojis
import os


# define costant files
X_LINKS = 'files/art_links/xefler_links.txt'
X_IMGS = 'imgs/xefler'
X_POSTED = 'files/art_links/xefler_posted.txt'

NOISE_GRAVITE_LINKS = 'files/art_links/gravite_links.txt'
NOISE_GRAVITE_IMGS = 'imgs/noise/gravite'
GRAVITE_POSTED = 'files/art_links/gravite_posted.txt'
NOISE_SOLIPSISM_LINKS = 'files/art_links/solipsism_links.txt'
NOISE_SOLIPSISM_IMGS = 'imgs/noise/solipsism'
SOLIPSISM_POSTED = 'files/art_links/solipsism_posted.txt'
NOISE_FAOONA_LINKS = 'files/art_links/faoona_links.txt'
NOISE_FAOONA_IMGS = 'imgs/noise/faoona'
FAOONA_POSTED = 'files/art_links/faoona_posted.txt'

MAC_KOMIKS_LINKS = 'files/art_links/komiks_links.txt'
MAC_KOMIKS_IMGS = 'imgs/mac'
KOMIKS_POSTED = 'files/art_links/komiks_posted.txt'


NFT_HASH = 'files/hashtags/nft_hashtags.txt'
OPENSEA_HASH = 'files/hashtags/opensea_hashtags.txt'
XTZ_HASH = 'files/hashtags/tezos_hashtags.txt'
AI_HASH = 'files/hashtags/ai_hashtags.txt'
GENART_HASH = 'files/hashtags/genart_hashtags.txt'


MAC_SHILL_LIST = 'files/shill_msgs/mac_shill_messages.txt'
MAC_SHILLED = 'files/shill_msgs/mac_posted_shills.txt'
EGON_SHILL_LIST = 'files/shill_msgs/egon_shill_messages.txt'
EGON_SHILLED = 'files/shill_msgs/egon_posted_shills.txt'
X_SHILL_LIST = 'files/shill_msgs/xefler_shill_messages.txt'
X_SHILLED = 'files/shill_msgs/xefler_posted_shills.txt'

LAST_LIKED_TWEET = 'files/last_seen_reply.txt'


#===============================================================================================
#============================= TWEET SHILLS & ART FUNCTIONS ====================================
#===============================================================================================

# use this function to tweet about NFT shills
def drop_me_NFTs(usr):
    # open the file that contains all the shilling tweets
    # read it line by line
    # choose one line from them using the never_twice function from keys_utils.py
    
    if(usr == "mac"):
         api = api_mac
         shills_read = open(MAC_SHILL_LIST, 'r')
         lines = shills_read.readlines()
         line = lines[never_twice(lines, MAC_SHILLED)]
    if(usr == "x"):
         api = api_x
         shills_read = open(X_SHILL_LIST, 'r')
         lines = shills_read.readlines()
         line = lines[never_twice(lines, X_SHILLED)]
    if(usr == "noise"):
         api = api_noise
         shills_read = open(EGON_SHILL_LIST, 'r')
         lines = shills_read.readlines()
         line = lines[never_twice(lines, EGON_SHILLED)]

    # split the tweet in pieces to have multiple lines tweets
    shill_ps = line.split(' - ')
    shill = ''

    for p in shill_ps:
        # do the emojis encoding
       shill += '\n'+emojis.encode(p)
    # try to update my status with it
    try:
        api.update_status(str(shill))
        # print the text how it got tweeted
        print(shill)
    # if you encounter a problem, console log it
    except tweepy.errors.HTTPException as e: 
        print('==================================================')
        print(e)
        print('==================================================')

# this function returns random hashtags from a specific list      
def get_random_hashtags(FILE):
    # open the file from the second argument and read it line by line
    file_read = open(FILE, 'r')
    lines = file_read.readlines()
    # try get a random number for the length of the list in the argument
    chance = random.randrange(len(lines)-1)
    hash = lines[chance]
    return hash
    
# this function gets a random NFT from the ones specified in a file
def get_random_nft(usr, opt):
    if(usr == "x" and opt == "reflections"):
        NFTS = X_IMGS 
        LINKS = X_LINKS 
        POSTED = X_POSTED
        hash1 = get_random_hashtags(OPENSEA_HASH)
        hash2 = get_random_hashtags(NFT_HASH)
    if(usr == "mac" and opt == "komiks"):
        NFTS = MAC_KOMIKS_IMGS 
        LINKS = MAC_KOMIKS_LINKS 
        POSTED = KOMIKS_POSTED
        hash1 = get_random_hashtags(OPENSEA_HASH)
        hash2 = get_random_hashtags(AI_HASH)
    if(usr == "noise" and opt == "gravite"): 
        NFTS = NOISE_GRAVITE_IMGS 
        LINKS = NOISE_GRAVITE_LINKS
        POSTED = GRAVITE_POSTED
        hash1 = get_random_hashtags(XTZ_HASH)
        hash2 = get_random_hashtags(GENART_HASH)
    if(usr == "noise" and opt == "solipsism"): 
        NFTS = NOISE_SOLIPSISM_IMGS 
        LINKS = NOISE_SOLIPSISM_LINKS
        POSTED = SOLIPSISM_POSTED
        hash1 = get_random_hashtags(XTZ_HASH)
        hash2 = get_random_hashtags(NFT_HASH)
    if(usr == "noise" and opt == "faoona"): 
        NFTS = NOISE_FAOONA_IMGS 
        LINKS = NOISE_FAOONA_LINKS
        POSTED = FAOONA_POSTED
        hash1 = get_random_hashtags(OPENSEA_HASH)
        hash2 = get_random_hashtags(NFT_HASH)

    # create a list from the lines in the file NFTS_PATH
    nfts_list = os.listdir(NFTS)
    # use the never_twice function to get one of them that has not been already posted
    pick_one = never_twice(nfts_list, POSTED)
    # saves the file name
    nft_jpg = str(nfts_list[pick_one])
    # creates the whole path to the file
    full_nft_path = NFTS+'/'+nft_jpg
    # print(nft_jpg)
    # opens the files with all the URLs
    with open(LINKS, 'r') as links_file:
        all_lines = links_file.readlines()
        for line in all_lines:
            # when it finds the url with the same name as the file
            # splits the line into the artwork's name and the url
            if nft_jpg in line:
                nft_name = line.split(' - ')[0]
                nft_link = line.split(' - ')[1] 
    # returning all the useful info gathered up to now  
    # print(full_nft_path)
    # print(nft_link)
    # print(nft_name)          
    return full_nft_path, nft_link, nft_name, hash1, hash2

# a function to tweet art on the profile
def tweet_art(usr, opt):
    if(usr == "x"): api = api_x
    if(usr == "noise"): api = api_noise
    if(usr == "mac"): api = api_mac

    try:
        # use function above to get a random nft to post
        nft = get_random_nft(usr, opt)
        # creates the tweet
        hashtags = "\n\n"+ str(nft[3]) + str(nft[4])
        media = api.media_upload(str(nft[0]))
        # updates the profile with the NFT just made
        api.update_status(status = nft[1] + hashtags, media_ids = [media.media_id])
        # console logs which NFT has been tweeted
        print('I tweeted this NFT on '+usr+' timeline: '+nft[2]+'\n')
    # logs the possible errors
    except tweepy.errors.HTTPException as e: 
        print('==================================================')
        print(e)
        print('==================================================')
        return False

    

tweet_art("noise", "solipsism")
# get_random_nft("noise")
# get_random_hashtags(GENART_HASH)
