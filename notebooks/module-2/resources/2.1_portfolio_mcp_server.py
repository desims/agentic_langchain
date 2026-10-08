from dotenv import load_dotenv

load_dotenv()

from mcp.server.fastmcp import FastMCP
from typing import Dict, Any
from requests import get

mcp = FastMCP("portfolio_server")


# Tool for getting SRTG portfolio
@mcp.tool()
def get_portfolio() -> list[str]:
    """Get the list of companies in the SRTG portfolio."""
    
    return [
        "TBIG",
        "MDKA",
        "ADRO",
        "AADI",
        "MPMX",
        "NRCA",
        "AGII",
    ]


if __name__ == "__main__":
    mcp.run(transport="stdio")
