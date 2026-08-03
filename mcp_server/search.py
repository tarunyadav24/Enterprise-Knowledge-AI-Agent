from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

from mcp_server.config import (
    AZURE_AI_SEARCH_ENDPOINT,
    AZURE_AI_SEARCH_KEY,
    AZURE_AI_SEARCH_INDEX_NAME,
)

# Create Search Client
search_client = SearchClient(
    endpoint=AZURE_AI_SEARCH_ENDPOINT,
    index_name=AZURE_AI_SEARCH_INDEX_NAME,
    credential=AzureKeyCredential(AZURE_AI_SEARCH_KEY),
)


def search_enterprise_documents(query: str):
    """
    Search enterprise documents from Azure AI Search
    """

    results = search_client.search(
        search_text=query,
        top=3,
    )

    documents = []

    for result in results:
        documents.append(dict(result))

    return documents