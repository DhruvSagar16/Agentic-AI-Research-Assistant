from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool
from datetime import datetime

# Custom save tool using decorator
@tool
def save_tool(data: str) -> str:
    """Saves structured research data to a text file. Call this only ONCE at the end."""
    # Check if this exact data was already saved
    try:
        with open("research_output.txt", "r", encoding="utf-8") as f:
            if data in f.read():
                return "Data already saved, skipping duplicate."
    except FileNotFoundError:
        pass

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    with open("research_output.txt", "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Data successfully saved to research_output.txt"

# Search tool
@tool
def search_tool(query: str) -> str:
    """Search the web for information"""
    search = DuckDuckGoSearchRun()
    return search.run(query)

# Wikipedia tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

