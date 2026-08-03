import json
from pathlib import Path

from mcp_server.search import search_enterprise_documents


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"


def get_company_policy():
    """
    Return company policy from JSON.
    """

    with open(DATA_DIR / "company_policy.json", "r", encoding="utf-8") as f:
        return json.load(f)


def get_holiday_calendar():
    """
    Return holiday calendar from JSON.
    """

    with open(DATA_DIR / "holiday_calendar.json", "r", encoding="utf-8") as f:
        return json.load(f)


def search_documents(query: str):
    """
    Search enterprise documents using Azure AI Search.
    """

    return search_enterprise_documents(query)