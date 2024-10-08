import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool as sb
from base64 import b64decode

load_dotenv()

DEVS = [
    607067484,  # Ayiin
    997461844,  # Punya Ayiin
    844432220,  # Risman
    883761960,  # Ari
    2130526178,  # Alfa
    1663258664,  # Kyy
]

GCAST_BLACKLIST = [
    -1001797285258,  # AyiinChats <- New
    -1001675396283,  # AyiinChats
    -1001473548283,  # SharingUserbot
    -1001361294038,  # UltroidSupportChat
    -1001387666944,  # PyrogramChat
    -1001109500936,  # TelethonChat
    -1001050982793,  # Python
    -1001256902287,  # DurovsChat
    -1001433238829,  # TedeSupport
    -1001642830120,  # Aditya Discus
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001459812644,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001788983303,  # KayzuSupport
    -1001380293847,  # NastySupport
    -1001692751821,  # RamSupport
    -1001267233272,  # PocongUserbot
    -1001500063792,  # Trident
    -1001687155877,  # CilikSupport
    -1001578091827,  # PrimeSupport
    -1001704645461,  # Jamet No Support
    -1001662510083,  # MutualanDestra
    -1001347414136,  # ArunaMutualan
    -1001572486389,  # PluviaMusicGroup
    -1001608701614,  # UputtSupport
    -1001812143750,  # Kynan Support
]

class Config(object):
    # Telegram App KEY and HASH
    API_KEY = int(getenv("API_KEY", "0"))
    API_HASH = getenv("API_HASH")

    # Inline bot helper
    BOT_TOKEN = getenv("BOT_TOKEN")
    BOT_USERNAME = getenv("BOT_USERNAME")

    OPENAI_API_KEY = getenv("OPENAI_API_KEY")

    # SUDO and Blacklist settings
    SUDO_USERS = {int(x) for x in getenv("SUDO_USERS", "").split()}
    BL_CHAT = {int(x) for x in getenv("BL_CHAT", "").split()}
    BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}

    # Default Blacklist Chats
    BLACKLIST_CHAT = [int(x) for x in (getenv("BLACKLIST_CHAT", "-1001473548283,-1001675396283")).split(",")]

    # Userbot Session String
    STRING_SESSION = getenv("STRING_SESSION")

    # Logging channel/group ID configuration
    BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "0"))

    # Load or No Load modules
    LOAD = getenv("LOAD", "").split()
    NO_LOAD = getenv("NO_LOAD", "").split()

    # Bleep Blop, this is a bot ;)
    PM_AUTO_BAN = sb(getenv("PM_AUTO_BAN", "True"))
    PM_LIMIT = int(getenv("PM_LIMIT", "6"))

    # Custom Handler command
    CMD_HANDLER = getenv("CMD_HANDLER", ".")
    SUDO_HANDLER = getenv("SUDO_HANDLER", r"$")

    # Support
    GROUP = getenv("GROUP", "BestieVirtual")
    CHANNEL = getenv("CHANNEL", "Nenen_degrees")

    # Heroku Credentials for updater
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY")

    # JustWatch Country
    WATCH_COUNTRY = getenv("WATCH_COUNTRY", "ID")

    # GitHub Credentials for updater and Gitupload
    GIT_REPO_NAME = getenv("GIT_REPO_NAME")
    GITHUB_ACCESS_TOKEN = getenv("GITHUB_ACCESS_TOKEN")

    # Custom (forked) repo URL for updater
    UPSTREAM_REPO_URL = getenv("UPSTREAM_REPO_URL", "https://github.com/xaikole/xaiko-userbot.git")

    # Custom Name Sticker Pack
    S_PACK_NAME = getenv("S_PACK_NAME")

    # SQL Database URI
    DB_URI = getenv("DATABASE_URL")
    DATABASE_PATH = os.path.join("ayiin.db")

    # OCR API key
    OCR_SPACE_API_KEY = getenv("OCR_SPACE_API_KEY")

    # remove.bg API key
    REM_BG_API_KEY = getenv("REM_BG_API_KEY", "jK9nGhjQPtd2Y5RhwMwB5EMA")

    # Chrome Driver and Headless Google Chrome Binaries
    CHROME_DRIVER = getenv("CHROME_DRIVER", "/usr/bin/chromedriver")
    GOOGLE_CHROME_BIN = getenv("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = getenv("OPEN_WEATHER_MAP_APPID")
    WEATHER_DEFCITY = getenv("WEATHER_DEFCITY", "Jakarta")

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(getenv("ANTI_SPAMBOT", "False"))
    ANTI_SPAMBOT_SHOUT = sb(getenv("ANTI_SPAMBOT_SHOUT", "False"))

    # Custom text for .alive command
    ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, Saya pengguna Fsyrl-Ubot")

    # Default .alive name
    ALIVE_NAME = getenv("ALIVE_NAME", "Fsyrl")

    # Custom Emojis for .alive command
    ALIVE_EMOJI = getenv("ALIVE_EMOJI", "✧")
    INLINE_EMOJI = getenv("INLINE_EMOJI", "✵")
    ICON_HELP = getenv("ICON_HELP", "⍟")

    # Time & Date - Country and Time Zone
    COUNTRY = getenv("COUNTRY", "ID")
    TZ_NUMBER = int(getenv("TZ_NUMBER", "1"))

    # Clean Welcome
    CLEAN_WELCOME = sb(getenv("CLEAN_WELCOME", "True"))

    # Zipfile module
    ZIP_DOWNLOAD_DIRECTORY = getenv("ZIP_DOWNLOAD_DIRECTORY", "./zips")

    # Bitly token
    BITLY_TOKEN = getenv("BITLY_TOKEN")

    # Bot version
    BOT_VER = getenv("BOT_VER", "4.0.0")

    # Default .alive logo
    ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph//file/b49aa34c29b05fe22d9c7.jpg")

    # Inline picture
    INLINE_PIC = getenv("INLINE_PIC", "https://telegra.ph//file/07fb28c1efb9058543241.jpg")

    # Picture For VCPLUGIN
    PLAY_PIC = getenv("PLAY_PIC", "https://telegra.ph/file/6213d2673486beca02967.png")
    QUEUE_PIC = getenv("QUEUE_PIC", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")

    # Default values
    DEFAULT = list(map(int, b64decode("MTkwNTA1MDkwMw==").split()))

    TEMP_DOWNLOAD_DIRECTORY = getenv("TMP_DOWNLOAD_DIRECTORY", "./downloads/")

    # Deezloader
    DEEZER_ARL_TOKEN = getenv("DEEZER_ARL_TOKEN")

    # NSFW Detect DEEP AI
    DEEP_AI = getenv("DEEP_AI")

    # Help command
    CMD_HELP = {
        "start": "Memulai bot",
        "help": "Menampilkan daftar perintah",
        # Tambahkan perintah lain sesuai kebutuhan
    }

var = Config()
