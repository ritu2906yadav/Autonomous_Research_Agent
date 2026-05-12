from typing import TypedDict,List

class ResearchState(TypedDict):
    query : str
    subtopics : List[str]
    search_result : List[str]
    summaries : List[str]
    final_report : str


