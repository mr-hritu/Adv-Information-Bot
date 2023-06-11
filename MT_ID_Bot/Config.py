import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6130457410:AAG8jDlWwyFQv1-u8XYnpDhtXaliPo3YrEY")


    API_ID = int(os.environ.get("API_ID", 29616312))


    API_HASH = os.environ.get("API_HASH", "dd1a05ab4c47a5a037cc067cf4bded27")


    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Private_Bots")


    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Prime_Hritu0_bot")
