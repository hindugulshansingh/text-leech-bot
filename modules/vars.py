import os

API_ID    = os.environ.get("API_ID", "26259762")
API_HASH  = os.environ.get("API_HASH", "6f33406b8cb80f659d268fccd7329b0f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
