import emojis
from keys_utils import write_to_file

# define txt files
NOISE_SHILLS="files/shill_msgs/egon_shill_messages.txt"
MAC_SHILLS="files/shill_msgs/mac_shill_messages.txt"
X_SHILLS="files/shill_msgs/xefler_shill_messages.txt"

shills = [
    "Drop your Art ๐๐ผโฌ๐ฅ",
    "Drop your NFT๐๐๐ค",
    "Drop me NFTs ๐ซถ๐ปโฌ๏ธ",
    "DROP your #NFTs + RT + COMMENT my pinned tweet ๐ฅ",
    "show me your new #NFT ๐ค๐ค ",
    "DROP your unsold #NFTs. Sells will come ๐๐ฅฐ๐",
    "Drop your NFT your majesty ๐โโ๏ธโฌ",
    "Drop some NFTs using #NFTsales! ๐",
    "DROP your cool NFT collection. Never give up โฌ๏ธโฌ๏ธโฌ๏ธ",
    "What's the latest NFT you've collected?",
    "So what I miss, anything new going on? \n(also shill thread โฌโฌโฌโฌ)",
    "Drop your awesome #NFT and shill it fast.",
    "drop your unsold NFT โค๏ธโ๐ฅโค๏ธโ๐ฅ๐ฏ๐ฏ #NFTs",
    "Drop some NFTs๐๐ป\nRTing the ones I like๐๐ป",
    "Hey, You?\nDrop some art now or go away.\n#NFT",
    "Drop your best nfts ๐โก",
    "Who makes really colorful art?\nTag/Drop it here (links welcome)\n๐",
    "I would like to see some artworks ๐๐",
    "Art Share Thread ๐งต\nDrop 1๏ธโฃ piece only ๐ผ๏ธ",
    "Just ART share ๐ซก๐",
    "Show me your fantastic #art โฌ๏ธ",
    "Drop your #NFT ๐ฝ\nโ Only NFT + price ( ETH | ฮ )\nโ Make friends, exchange follows & RTs\nโ RT this tweet\nโ Add entries to your shopping list\nโ Do not DM collectors",
    "FOLLOW ME ON INSTAGRAM ๐ฅ๐\n๐ธ https://instagram.com/egonisnoise.eth",
    "Drop your latest arts #NFT ๐๐",
    "Drop your #NFT๐Find you a buyer!",
    "DROP your NFT โฎ๏ธ๐ค\nShare your amazing art and show some support!",
    "Drop your lucky #NFTs ๐ฅ๐ฅ",
    "Share you most recent #NFT โก\nRT + FOLLOW for exposure #NFTCommunity",
    "ART SHARE! One image or video with title ๐ RT for others to see ๐",
    "WANTED: HOT ART FROM 2022 ARTIST DOING NFT ๐๐ป",
    "Can i see your unsold NFT? I'm going to retweet some!๐",
    "Drop your NFT ๐๐๐\nI'll RT as much as possible ๐ฆฅโค๏ธ",
    "Show me NFTs under 3.5 ETH",
    "Show me your art / NFTs โฌ๏ธ๐ฅ",
    "Drop #NFT for new artist ",
    "Show me your best #NFT โค๏ธ\nDrop below โคต๏ธโคต๏ธ",
    "Drop your #NFT under 2 ETH ๐",
    "#shill your polygon NFTs ๐",
    "How long have you been in NFTs?",
    "DROP your most recent NFT ๐ฅโฌ๏ธ๐๐ผ",
]

def create_shill_tweets(FILE):
    for shill in shills:
        decoded = emojis.decode(shill)
        fixed = decoded.replace("\n", " - ")
        write_to_file(FILE, fixed)

create_shill_tweets(NOISE_SHILLS)