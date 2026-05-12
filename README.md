# 🧠 Autonomous Research Agent

An AI-powered autonomous research assistant that can analyze user queries, search and retrieve relevant information, summarize insights, verify findings, and generate intelligent reports using LLMs and workflow-based AI agents.

---

# 🎯 Project Goal

Build an AI system that can:

- Understand a research query
- Plan research tasks
- Search the web
- Retrieve and summarize information
- Verify findings
- Generate a final report
- Maintain memory/history

---

# ⚙️ Final Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Workflow Engine | LangGraph |
| LLM | Groq |
| Framework | LangChain |
| Vector DB | ChromaDB |
| Embeddings | Sentence Transformers |
| Search API | Tavily |
| Memory | SQLite |
| PDF Support | PyPDFLoader |

---

# 🏗️ Project Architecture

```text
User Query
    ↓
Planner Agent
    ↓
Search Agent
    ↓
Retriever Agent
    ↓
Summarizer Agent
    ↓
Fact Checker Agent
    ↓
Report Generator Agent
    ↓
Final Report
```

---

# 📂 Project Structure

```bash
autonomous_research_agent/
│
├── agents/
│   ├── planner.py
│   ├── search_agent.py
│   ├── summarizer.py
│   ├── fact_checker.py
│   └── report_generator.py
│
├── tools/
│   ├── web_search.py
│   ├── vector_store.py
│   └── pdf_loader.py
│
├── app.py
├── workflow.py
├── state.py
├── requirements.txt
└── .env
```

---

# ✨ Features

- Multi-Agent AI Workflow
- Autonomous Research Planning
- Web Search Integration
- PDF Document Analysis
- Semantic Search with Vector Database
- Fact Verification System
- AI-Based Report Generation
- Memory and Context Tracking

---

# 🚀 Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

---

# 📸 Demo

Add screenshots or GIFs here.

```md
Screenshots/Screenshot1.png
screenshots/Screenshot 2.png
```

---

# 🌟 Future Improvements

- Multi-modal research support
- PDF report export
- Citation generation
- Real-time streaming responses
- Advanced memory systems
- Multi-user support
