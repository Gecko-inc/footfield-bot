import asyncio
import requests
from bot_app.data_fetcher import get_config

# TOKEN = asyncio.run(get_config()).get("bot_token")
TOKEN = requests.get("http://127.0.0.1:8000/api/get_config/").json().get("bot_token")
