from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","20787644"))
API_HASH = getenv("API_HASH","9dada820698e8a5fdd5e6cc78fac8567")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID","7050270303"))

MONGO_DB_URI = getenv("mongodb+srv://vivek:1234567890@cluster0.c48d8ih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN","WORLD_ALPHA")
