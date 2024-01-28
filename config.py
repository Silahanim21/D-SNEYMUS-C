import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "21197428"
API_HASH = "67e076ff6d2aac96451cfb961a313287"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6876097941:AAGPwyVdUrlzQEQU1Jd5Hv482OWCGYF0FSw")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ce3421:ce3421@cluster0.5dx4tcx.mongodb.net/test?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1800))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002112138580
LOG = 2
# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID","5693410792" ))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", 
    "https://github.com/ayaz2112/Dene"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/golgeharemileri")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/golgeharemileri")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None) 


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
 

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

 
# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION","AQCHwcxO-cD96C1YoNhLpy1nDjlZutO6oBP6hOeCCZDve-JO_UtJEYG4wDUbNwRh1X83v91dsQyPUierZcLeBaq7jGvjfrpQedn2nhLw9uTRznQ1xPKf_IVN9LAGK9uVlQoB3dUR3oh2N_wrpW3woCjfnY0p3Jthh1_ywAiweCSZZMb1d1WCspj7ZoZ7Bbjg6T_u9Uen7yyA3n_RxYfMP5ty0zII53p3UfGu8vQUoL4V7OCyQc3RoVIeOsxKPR0xngw5wNUdlTr4Ii3B942aVPy4lKdIYmqvsGeMQnSzscQggG9Q5z21xtiySgQjw7sQkEh66-qoqyXgPllrpU7YJbq1AAAAAZQUyKoA")
STRING2 = getenv("STRING_SESSION2", "AQCHwcxO-cD96C1YoNhLpy1nDjlZutO6oBP6hOeCCZDve-JO_UtJEYG4wDUbNwRh1X83v91dsQyPUierZcLeBaq7jGvjfrpQedn2nhLw9uTRznQ1xPKf_IVN9LAGK9uVlQoB3dUR3oh2N_wrpW3woCjfnY0p3Jthh1_ywAiweCSZZMb1d1WCspj7ZoZ7Bbjg6T_u9Uen7yyA3n_RxYfMP5ty0zII53p3UfGu8vQUoL4V7OCyQc3RoVIeOsxKPR0xngw5wNUdlTr4Ii3B942aVPy4lKdIYmqvsGeMQnSzscQggG9Q5z21xtiySgQjw7sQkEh66-qoqyXgPllrpU7YJbq1AAAAAZQUyKoA")
STRING3 = getenv("STRING_SESSION3", "BABXiBrVSlKncaJOSqZn6J_rghY_CjhlhgAvZFn0bxajF8WZCs8Yx48l0Ujq7MYs2JuTWM8ukxG5f2rAMw676Nn2VQI8BoH6WW54pvhqTPLYPn6UnOaKJVGBldmnrOi7RGNSuSfMOI8jv7KOpSWVAY_9KFGtJz162-Y4auweA_lFBXDZ81DvTnLYtgtBqr9tQYCpCp78T4dbxk3Pay2DTNjUGBIVIGmADoBqSE_wxXKrIY67whsvwzOC624VJnHKkyCZt71oEQZ_zSd6RiRRMZsP3LoJhhoQFGGr5aUfO6LKHzKXmpFa5Ffu9d4ALMd5QadeGtORKKlrYDj1VDirjKwEAAAAAYgLxfEA")
STRING4 = getenv("STRING_SESSION4", "BAAd4lA2DiBZ7iVw1WtghxrhrVVyTNrVhlH4gTMhJP90B4rfEUBMMRwYZvVSxZI_8GvcYZmMjIiW0kjK3Eab9hLBg0M3jqk2BaIkbdWMKF-OZTzrE0OP4uMxmTYR2a3JVYscxizHr9jmdjUoaYW1IA8f4O2GsKrShrFgWI826z_cGVpfD-uo4riuHShVoqKKV7XNtme-RWXx1s9rcrAYTzGdSrzpAGjzvBFh_qIFP4rihpl0y0zToTLvjK4nxCVoP96bOLVnDqftt-bdLKuKHWXFd2p6XnebBob0MQ1RHwRXxlxaS3cR-tx26WoCpWrwvbHHWlOSn8waGOiBv8N51Y_ZAAAAAZAZ640A")
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/ff564784dc65b2e867b2d.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL","https://graph.org/file/ec604b9b0030bb8806af4.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = ""
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        
if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
    )
