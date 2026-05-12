from llm import llm

def fact_checker_agent(state):
    summaries = state["summaries"]
    verified = []

    for summary in summaries:
        prompt = f"""
        Verify if this information appear reliable 

        Summary : 
        {summary}

        Mention possible in accuracies.

        """
        response = llm.invoke(prompt)
        verified.append(response.content)

    return {
        "summaries"  :verified
    }