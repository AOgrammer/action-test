import json
import os
from urllib.request import Request, urlopen

def post_discord(messages: list):
    webhook_url = os.getenv('WEBHOOK_URL')
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (private use) Python-urllib/3.10",
    }
    for message in messages:
        data = {"content": message}
        request = Request(
            webhook_url,
            data=json.dumps(data).encode(),
            headers=headers,
        )

        urlopen(request)
