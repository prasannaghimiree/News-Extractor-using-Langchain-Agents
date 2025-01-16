import json
from langchain.tools import tool
from langchain_community.utilities import SearxSearchWrapper

# Tool 1: Search Tool
@tool
def search_tool(query: str) -> str:
    """
    A searching tool that uses Searx to fetch information from the web.
    If your query is related to web searching, the agent uses this tool to fetch results.
    """
    try:
        # Connect to the local Searx instance
        s = SearxSearchWrapper(searx_host="http://search:8080") 
        return s.run(query)
    except Exception as e:
        return f"Error while searching: {str(e)}"

# Tool 2: Formatter Tool
@tool
def formatter(raw_text: str) -> dict:
    """
    Converts raw text data into a structured JSON format.
    
    The input should be a JSON string containing information such as headline, 
    author, publication date, event date, content, and source URL.
    Provide the answer in json format with specific headlines, and important events. 
    read {{raw_text}} and convert it into dictionary by putting all details.
    """
    try:
        data = json.loads(raw_text)
        
        if not isinstance(data, dict):
            raise ValueError("Parsed input is not a dictionary")
        return data  

    except Exception as e:
        return {"error": f"Formatting failed: {str(e)}"}

# Export tools
tools = [search_tool, formatter]

