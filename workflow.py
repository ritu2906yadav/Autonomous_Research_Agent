from langgraph.graph import StateGraph,END
from state import ResearchState

from agents.planner import planner_agent
from agents.search_agent import search_agent
from agents.summarizer import summarizer_agent
from agents.fact_checker import fact_checker_agent
from agents.report_generator import report_generator_agent 

workflow = StateGraph(ResearchState)

workflow.add_node("planner",planner_agent)
workflow.add_node("search",search_agent)
workflow.add_node("summarizer",summarizer_agent)
workflow.add_node("fact_checker",fact_checker_agent)
workflow.add_node("report_generator",report_generator_agent)

workflow.set_entry_point("planner")
workflow.add_edge("planner","search")
workflow.add_edge("search","summarizer")
workflow.add_edge("summarizer","fact_checker")
workflow.add_edge("fact_checker","report_generator")
workflow.add_edge("report_generator",END)

app = workflow.compile()