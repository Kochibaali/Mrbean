import re
import os
from os import environ
from pyrogram import enums
from Script import script

import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
SESSION = 'Media_search'
API_ID = int(18674011)
API_HASH = "38d3664512757d8830601169eff5a1de"
BOT_TOKEN = "5491810950:AAG6Nhr-8kSCjVPDYLIKEdahA_zyTrARVXY"
false =  False
# Bot settings
CACHE_TIME = int(300)
USE_CAPTION_FILTER = False
PICS = ('https://telegra.ph/file/2992a480cae2bc0de1c39.jpg https://telegra.ph/file/76e7b5e94430b84a3d2b2.jpg https://telegra.ph/file/3544a8773740b0412c9dd.jpg https://telegra.ph/file/4b1c7004ea8bd3fed8df9.jpg https://telegra.ph/file/a02e47d932adc336740fa.jpg').split()
NOR_IMG = "https://telegra.ph/file/7d7cbf0d6c39dc5a05f5a.jpg"
SPELL_IMG = "https://telegra.ph/file/b58f576fed14cd645d2cf.jpg"

# Welcome area
MELCOW_IMG = "https://telegra.ph/file/e54cae941b9b81f13eb71.jpg"
MELCOW_VID = ""


# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in (1099497360,5583768837,6446790411).split()
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in [-1001477932100,-1001975909776]
auth_users = [int(user) if id_pattern.search(user) else user for user in ('')
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = ''
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = ''
# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = "./DOWNLOADS/"

# FSUB
auth_channel = "-1001934799142"
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# Command
COMMAND_HAND_LER = "/"

# MongoDB information
DATABASE_URI = "mongodb+srv://U:U@cluster0.qg0zqam.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = 'Telegram_files'
MONGO_URL = ""

#Downloader
DOWNLOAD_LOCATION = "./DOWNLOADS/AudioBoT/"

#url links
SHORTLINK_URL = 'shorturllink.in'
SHORTLINK_API = '3a3935e37c74a2384f7a689c414f078ab6320785'
IS_SHORTLINK = bool(False)

#Auto approve 
#In private group or channel must enable request admin approval 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in '0']
TEXT = "Hello {mention}\nWelcome To {title}\n\nYour request has been approved"
APPROVED = "off"

# Others
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in '-1001275345753']
PORT = "8080"
MAX_BTN = int(10)
S_GROUP = "https://t.me/new_movies_group_2021"
MAIN_CHANNEL = "https://t.me/new_movies_group_2021"
FILE_FORWARD = "https://t.me/+1dbVg9pA2GphZmI1"
MSG_ALRT = '𝑪𝑯𝑬𝑪𝑲 & 𝑻𝑹𝒀 𝑨𝑳𝑳 𝑴𝒀 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺'
FILE_CHANNEL = int(0)
LOG_CHANNEL = int(-1001934799142)
SUPPORT_CHAT = 'https://t.me/new_movies_group_2021'
AUTO_DELETE = is_enabled(False, False)
P_TTI_SHOW_OFF = is_enabled(False, False)
IMDB = is_enabled(True, True)
SINGLE_BUTTON = is_enabled(True, True)
CUSTOM_FILE_CAPTION = f"{script.CUSTOM_FILE_CAPTION}"
BATCH_FILE_CAPTION = CUSTOM_FILE_CAPTION
IMDB_TEMPLATE = f"{script.IMDB_TEMPLATE_TXT}"
LONG_IMDB_DESCRIPTION = is_enabled(False, False)
SPELL_CHECK_REPLY = is_enabled(True, True)
MAX_LIST_ELM = None
INDEX_REQ_CHANNEL = int(LOG_CHANNEL)
FILE_STORE_CHANNEL = [int(ch) for ch in ('').split()]
MELCOW_NEW_USERS = is_enabled(True, True)
PROTECT_CONTENT = is_enabled(False, False)
PUBLIC_FILE_STORE = is_enabled(True, True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}
