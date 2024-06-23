from github_api import fetch_ready_items
from discord_api import post_discord

if __name__ == "__main__":
    ready_items = fetch_ready_items()
    post_discord(ready_items)
