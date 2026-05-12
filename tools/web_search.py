from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os

load_dotenv()

search_tool =  TavilySearchResults(
    tavily_api_key=os.getenv("TAVILY_API_KEY"),
    max_results= 5
)

