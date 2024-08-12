import os


class Config:
    API_ID = int(os.environ.get("API_ID", 20077058))  # Change 12345 to your API_ID
    API_HASH = os.environ.get("API_HASH", "349639880eb5b1cb0ff6c2b8a6f16717")  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7330436352:AAHUJUNGytd9bTY1otHe7EVwJlN4km0usXw")  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", 6169288210))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", "ؖؖؖؖؖؖؖؖؖ𓆪:ᵛ͢ᵎᵖ ┋ﷺ آلُـِـِِـِِِـِِـِـﮩرمـْـْْـْ آلُـِـِِـِِِـِِـِـڛـ,ـآبـٌـٌٌـٌٌٌـٌٌـٌعٌ ﷺ┋[ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ")  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @MysteryBotsChat.
