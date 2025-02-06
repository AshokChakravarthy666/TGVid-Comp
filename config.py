import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", 15657755 )  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "7cce51d4664d010b90ad690e0d5121ad") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7794041196:AAF38WlKwzNTJkfZq2iF93hj9p4cORtPsPI") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002440769217') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6650849235")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002351435664')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
