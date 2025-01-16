from langchain_core.tools import tool
from langchain_community.utilities import SearxSearchWrapper
import json

@tool
def search_tool(query: str) -> str:
    """
    This is a searching tool. If your query is related to web searching, the agent uses this tool to fetch information.
    """
    try:
        s = SearxSearchWrapper(searx_host="http://search:8080") 
        return s.run(query)
    except Exception as e:
        return f"Error while searching: {str(e)}"


@tool
def formatter(raw_text: str) -> dict:
    '''
    This tool converts raw text data into a structured JSON format.

    The input should be a JSON string containing information such as headline, author, publication date, event date, content, and source URL.
    The tool parses the input and returns it as a Python dictionary.
    '''
    try:
        data = json.loads(raw_text)

        
        if not isinstance(data, dict):
            raise ValueError("Parsed input is not a dictionary")

        return data  

    except Exception as e:
    
        return {"error": f"Formatting failed: {str(e)}"}

   
tools = [formatter, search_tool]