from fastmcp import FastMCP
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Create MCP Server
# --------------------------------------------------

mcp = FastMCP("AWO MCP Demo")

# --------------------------------------------------
# Load dataset once
# --------------------------------------------------

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "facilities.csv"

try:
    df = pd.read_csv(DATA_PATH, dtype=str).fillna("")
    print(f"Loaded {len(df)} facilities")
except FileNotFoundError:
    print(f"Dataset not found: {DATA_PATH}")
    df = pd.DataFrame()


# --------------------------------------------------
# Helper
# --------------------------------------------------

def format_facility(row):
    return f"""
Name: {row['name']}
City: {row['city']}
Postcode: {row['postcode']}
Phone: {row['phone']}
Email: {row['email']}
Website: {row['website']}
Service: {row['service']}
"""


# --------------------------------------------------
# Tool 1
# --------------------------------------------------

@mcp.tool()
def count_facilities(city: str) -> int:
    """
    Count the number of facilities in a given city.
    """

    if df.empty:
        return 0

    return df[
        df["city"].str.casefold() == city.casefold()
    ].shape[0]


# --------------------------------------------------
# Tool 2
# --------------------------------------------------

@mcp.tool()
def search_facilities(city: str) -> str:
    """
    Return all facilities in a given city.
    """

    if df.empty:
        return "Dataset not available."

    results = df[
        df["city"].str.casefold() == city.casefold()
    ]

    if results.empty:
        return f"No facilities found in '{city}'."

    return "\n-------------------------\n".join(
        format_facility(row)
        for _, row in results.iterrows()
    )


# --------------------------------------------------
# Tool 3
# --------------------------------------------------

@mcp.tool()
def find_facilities_by_service(service: str) -> str:
    """
    Search facilities by service type.
    """

    if df.empty:
        return "Dataset not available."

    results = df[
        df["service"].str.contains(
            service,
            case=False,
            na=False,
        )
    ]

    if results.empty:
        return f"No facilities provide '{service}'."

    return "\n-------------------------\n".join(
        format_facility(row)
        for _, row in results.iterrows()
    )


# --------------------------------------------------

if __name__ == "__main__":
    mcp.run()