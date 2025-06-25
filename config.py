import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7971094918:AAFA47AQkv0jZrGB8T_stCt_jJxBx6uRzsU")
API_ID = int(os.environ.get("API_ID", "28202735"))
API_HASH = os.environ.get("API_HASH", "ad753434fda6713ec7d840d1c60dcae9")


OWNER_ID = int(os.environ.get("OWNER_ID", "1454860223"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://anisalynch20:fGCU0snOtdkiujsI@jovay.h6l2f.mongodb.net/?retryWrites=true&w=majority&appName=jovay")
DB_NAME = os.environ.get("DB_NAME", "anisalynch20")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002608642218"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002290424393"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002447613053"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "0")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[1454860223]
    for x in (os.environ.get("ADMINS", "1454860223").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "False") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌jangan spam bang"

START_MSG = os.environ.get("START_MESSAGE", "Hallo {mention}\n\nada apa bang😹")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE",     """Hallo {mention}

<b>Anda harus bergabung di Channel/Grup saya terlebih dahulu untuk melihat film yang saya bagikan...</b>

<b><blockquote>Silakan Join Ke Channel & Group Terlebih Dahulu</b></blockquote>
"""
)




ADMINS.append(OWNER_ID)
ADMINS.append(6848088376)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
