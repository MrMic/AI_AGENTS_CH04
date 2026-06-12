from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from typing import List


def web_search(web_query: str, num_results: int) -> List[str]:
    """
    Perform a web search using DuckDuckGo and return the results.

    Args:
        web_query (str): The search query to be performed.
        num_results (int): The number of search results to return.

    Returns:
        List[str]: A list of search result URLs.
    """

    return [
        r["link"] for r in DuckDuckGoSearchAPIWrapper().results(web_query, num_results)
    ]
