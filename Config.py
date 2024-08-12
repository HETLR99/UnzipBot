import os


class Config:
    API_ID = int(os.environ.get("API_ID", 16536417))  # Change 12345 to your API_ID
    API_HASH = os.environ.get("API_HASH", "f6e58a549da642d7b765744a2f82c6d9")  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7330436352:AAHUJUNGytd9bTY1otHe7EVwJlN4km0usXw")  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", 6169288210))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", "ؖؖؖؖؖؖؖؖؖ𓆪:ᵛ͢ᵎᵖ ┋ﷺ آلُـِـِِـِِِـِِـِـﮩرمـْـْْـْ آلُـِـِِـِِِـِِـِـڛـ,ـآبـٌـٌٌـٌٌٌـٌٌـٌعٌ ﷺ┋[ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ")  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @MysteryBotsChat.
