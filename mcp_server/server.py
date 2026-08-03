from fastmcp import FastMCP
from mcp_server.tools import (
    get_company_policy,
    get_holiday_calendar,
    search_documents,
)

mcp = FastMCP("Enterprise Knowledge MCP")


@mcp.tool
def company_policy():
    """Get company policy."""
    return get_company_policy()


@mcp.tool
def holiday_calendar():
    """Get holiday calendar."""
    return get_holiday_calendar()


@mcp.tool
def enterprise_search(query: str):
    """Search enterprise documents."""
    return search_documents(query)


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        path="/mcp",
    )