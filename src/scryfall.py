import aiohttp

SCRYFALL_NAMED_URL = "https://api.scryfall.com/cards/named"


async def fetch_card(session: aiohttp.ClientSession, name: str) -> dict | None:
    """Fetch a card by name from Scryfall. Returns card data or None if not found."""
    async with session.get(SCRYFALL_NAMED_URL, params={"fuzzy": name}) as resp:
        if resp.status == 200:
            return await resp.json()
        return None


def format_card_link(card: dict) -> str:
    return f"**{card['name']}**: {card['scryfall_uri']}"
