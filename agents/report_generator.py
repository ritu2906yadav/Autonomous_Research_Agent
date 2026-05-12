from llm import llm

def report_generator_agent(state):
    summaries = state["summaries"]
    query  = state["query"]

    combined = "\n".join(summaries)
    prompt = f"""
    Generate a professional research report.

    Topic:
    {query}

    Research:
    {combined}

    Include:
    - Introduction
    - Main Findings
    - challenges
    - Future Scope 
    - Conclusions
    """

    response = llm.invoke(prompt)

    return {
        "final_report" : response.content
    }