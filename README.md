This is a twitter bot to promotes 3 different accounts for NFTs and digital art.
The whole of the work was done with the tweepy API. 

The tasks the bot can do over multiple accounts are:
- tweet open ended questions
- tweet art pseudo-randomly from folders of images, connect them to a selling point URL and check that every single image in the folder has been tweeted      once before re-starting the process
- like the answers to the specified account tweets and random tweets from the profiles that replied 
- count the number of likes of the accounts last 10 previous tweets and retweet the most popular
- retweet art from a specified, ever-growing list of favorite accounts 
- update the counts of followers and following profiles, rank the most popular and find their followers
- like and retweet the tweets of the accounts in the "network"

All of this is done asynchronously, while checking for connection and API errors and the routines never stop.

Of course NFT images and keys have been removed from this repository.
Any future update to the working model of this "multi bot" will be kept private.
This repo is only for the purpose of showcasing my Python API skills, one of the working twitter accounts applying this code can be found here:

https://twitter.com/shiller_mac

EVERY single action performed by his account is automated.
