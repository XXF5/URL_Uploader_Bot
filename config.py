import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "7252762683:AAHUfR4-oAzTzS_94fq6ygoHRB_EG1lW6E4") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", 26545740)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "108df940118cde6c5f524f4d439a19d3") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 6169288210)) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "mongodb+srv://mrhex86:mrhex86@cluster0.8pxiirj.mongodb.net") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)
