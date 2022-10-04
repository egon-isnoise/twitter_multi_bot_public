import emojis
from keys_utils import write_to_file

# define txt files
NOISE_SHILLS="files/shill_msgs/egon_shill_messages.txt"
MAC_SHILLS="files/shill_msgs/mac_shill_messages.txt"
X_SHILLS="files/shill_msgs/xefler_shill_messages.txt"

shills = [
    "Drop your Art 👇🏼⏬🔥",
    "Drop your NFT💎😍🤟",
    "Drop me NFTs 🫶🏻⬇️",
    "DROP your #NFTs + RT + COMMENT my pinned tweet 💥",
    "show me your new #NFT 🤑🤠",
    "DROP your unsold #NFTs. Sells will come 📈🥰👇",
    "Drop your NFT your majesty 🙇‍♀️⏬",
    "Drop some NFTs using #NFTsales! 👇",
    "DROP your cool NFT collection. Never give up ⬇️⬇️⬇️",
    "What's the latest NFT you've collected?",
    "So what I miss, anything new going on? \n(also shill thread ⏬⏬⏬⏬)",
    "Drop your awesome #NFT and shill it fast.",
    "drop your unsold NFT ❤️‍🔥❤️‍🔥💯💯 #NFTs",
    "Drop some NFTs👇🏻\nRTing the ones I like👍🏻",
    "Hey, You?\nDrop some art now or go away.\n#NFT",
    "Drop your best nfts 👇⚡",
    "Who makes really colorful art?\nTag/Drop it here (links welcome)\n👇",
    "I would like to see some artworks 😍👇",
    "Art Share Thread 🧵\nDrop 1️⃣ piece only 🖼️",
    "Just ART share 🫡👇",
    "Show me your fantastic #art ⬇️",
    "Drop your #NFT 🔽\n✅ Only NFT + price ( ETH | Ξ )\n✅ Make friends, exchange follows & RTs\n✅ RT this tweet\n✅ Add entries to your shopping list\n❌ Do not DM collectors",
    "FOLLOW ME ON INSTAGRAM 🔥👇\n🔸 https://instagram.com/egonisnoise.eth",
    "Drop your latest arts #NFT 🚀👇",
    "Drop your #NFT👇Find you a buyer!",
    "DROP your NFT ☮️🤛\nShare your amazing art and show some support!",
    "Drop your lucky #NFTs 🔥🔥",
    "Share you most recent #NFT ⚡\nRT + FOLLOW for exposure #NFTCommunity",
    "ART SHARE! One image or video with title 🙏 RT for others to see 🙌",
    "WANTED: HOT ART FROM 2022 ARTIST DOING NFT 👇🏻",
    "Can i see your unsold NFT? I'm going to retweet some!🙏",
    "Drop your NFT 👇👇👇\nI'll RT as much as possible 🦥❤️",
    "Show me NFTs under 3.5 ETH",
    "Show me your art / NFTs ⬇️🔥",
    "Drop #NFT for new artist ",
    "Show me your best #NFT ❤️\nDrop below ⤵️⤵️",
    "Drop your #NFT under 2 ETH 🌈",
    "#shill your polygon NFTs 👀",
    "How long have you been in NFTs?",
    "DROP your most recent NFT 🔥⬇️👋🏼",
]

def create_shill_tweets(FILE):
    for shill in shills:
        decoded = emojis.decode(shill)
        fixed = decoded.replace("\n", " - ")
        write_to_file(FILE, fixed)

create_shill_tweets(NOISE_SHILLS)