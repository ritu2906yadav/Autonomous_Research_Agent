from llm import llm

def summarizer_agent(state):
    search_results = state.get("search_results",[])

    summaries = []

    for result in search_results:
        
        prompt = f"""
        Summarize this

       
        {result}
        """
        
        response = llm.invoke(prompt)
        summaries.append(response.content)

    return {
        "summaries" : summaries
    }
