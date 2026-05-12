from llm import llm

def planner_agent(state):
    query = state["query"]
    prompt = f""" Break the reasearch topic into importent subopic
    Topic:
    {query}
    
    Return bullet points
    """

    response = llm.invoke(prompt)
    subtopics = response.content.split("\n")

    return {
        "subtopics": subtopics
    }
    


