from tools.web_search import search_tool

def search_agent(state):
    subtopics = state["subtopics"]
    
    results = []


    for topic in subtopics:
        search_result = search_tool.invoke(topic)
        
        results.append(str(search_result))

    
    return {
        "search_results": results
    }

        