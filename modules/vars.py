from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("23163380")
API_HASH = getenv("2dca155e786c7db2d295e5b4ab10783b")
BOT_TOKEN = getenv("6943434912:AAHmi_GEa7_uHuJnvVfeslJhPHl-ezlKWVc")
OWNER_ID = int(getenv("5827915041")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1368753935").split()))
