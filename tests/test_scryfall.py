from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.scryfall import fetch_card, format_card_link


@pytest.fixture
def mock_card():
    return {
        "name": "Lightning Bolt",
        "scryfall_uri": "https://scryfall.com/card/lea/161/lightning-bolt",
    }


class TestFetchCard:
    async def test_returns_card_data_on_success(self, mock_card):
        mock_resp = AsyncMock()
        mock_resp.status = 200
        mock_resp.json = AsyncMock(return_value=mock_card)
        mock_resp.__aenter__ = AsyncMock(return_value=mock_resp)
        mock_resp.__aexit__ = AsyncMock(return_value=False)

        mock_session = MagicMock()
        mock_session.get = MagicMock(return_value=mock_resp)

        result = await fetch_card(mock_session, "Lightning Bolt")
        assert result == mock_card

    async def test_returns_none_on_404(self):
        mock_resp = AsyncMock()
        mock_resp.status = 404
        mock_resp.__aenter__ = AsyncMock(return_value=mock_resp)
        mock_resp.__aexit__ = AsyncMock(return_value=False)

        mock_session = MagicMock()
        mock_session.get = MagicMock(return_value=mock_resp)

        result = await fetch_card(mock_session, "Not A Real Card")
        assert result is None


class TestFormatCardLink:
    def test_formats_name_and_uri(self, mock_card):
        result = format_card_link(mock_card)
        assert result == "**Lightning Bolt**: https://scryfall.com/card/lea/161/lightning-bolt"
