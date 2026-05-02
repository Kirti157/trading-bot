from binance.client import Client
import os
import time
from dotenv import load_dotenv

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET")
)

# Correct testnet setup
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# Fix timestamp safely
try:
    server_time = client.futures_time()
    client.timestamp_offset = server_time['serverTime'] - int(time.time() * 1000)
except:
    client.timestamp_offset = 0