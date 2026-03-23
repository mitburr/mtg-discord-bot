# mtg-discord-bot

Discord bot that detects MTG card names in `[[double brackets]]` and replies in a thread with Scryfall links.

## Quick Start

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill in DISCORD_BOT_TOKEN
task start
```

## Usage

In any channel the bot can read, wrap card names in double brackets:

```
I'm thinking of running [[Lightning Bolt]] and [[Counterspell]] in this list.
```

The bot will create a thread on your message with Scryfall links for each card (up to 5 per message). Fuzzy matching handles typos.

## Discord Setup

1. Create a bot at [discord.com/developers/applications](https://discord.com/developers/applications)
2. Enable **Message Content Intent** under Bot → Privileged Gateway Intents
3. Invite with scopes: `bot` + permissions: `Send Messages`, `Read Message History`, `Create Public Threads`, `Send Messages in Threads`
4. Copy the bot token into `.env`

## Deployment

Runs as a systemd service on Sequoia. See `docs/ai/` for deployment notes.
