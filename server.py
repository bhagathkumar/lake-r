# server.py

from mcp.server.fastmcp import FastMCP
import utils.file_reader as utils

mcp = FastMCP("mix_server") 
# Entry point to run the server

@mcp.tool()
def summarize_csv_file(filename: str) -> str:
    """
    Summarize a CSV file by reporting its number of rows and columns.
    Args:
        filename: Name of the CSV file in the /data directory (e.g., 'sample.csv')
    Returns:
        A string describing the file's dimensions.
    """
    return utils.read_csv_summary(filename)

@mcp.tool()
def summarize_parquet_file(filename: str) -> str:
    """
    Summarize a Parquet file by reporting its number of rows and columns.
    Args:
        filename: Name of the Parquet file in the /data directory (e.g., 'sample.parquet')
    Returns:
        A string describing the file's dimensions.
    """
    return utils.read_parquet_summary(filename)


if __name__ == "__main__":
    mcp.run()