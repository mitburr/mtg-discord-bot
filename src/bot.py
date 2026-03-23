import os
import re

import aiohttp
import discord
from dotenv import load_dotenv

from src.scryfall import fetch_card, format_card_link

load_dotenv()

CARD_PATTERN = re.compile(r"\[\[(.+?)\]\]")
MAX_CARDS_PER_MESSAGE = 5

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    cards = CARD_PATTERN.findall(message.content)[:MAX_CARDS_PER_MESSAGE]
    if not cards:
        return

    async with aiohttp.ClientSession() as session:
        results = []
        for name in cards:
            card = await fetch_card(session, name)
            if card:
                results.append(format_card_link(card))
            else:
                results.append(f"Card not found: `{name}`")

    if results:
        thread = await message.create_thread(name="Card Links", auto_archive_duration=60)
        await thread.send("\n".join(results))


def main():
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_BOT_TOKEN not set")
    client.run(token)


if __name__ == "__main__":
    main()
