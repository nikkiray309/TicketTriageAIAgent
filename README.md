# Support Ticket Triage Agent

## Overview

Support Ticket Triage Agent is an AI-powered assistant that helps support engineers analyze customer tickets, identify the issue category, retrieve relevant troubleshooting guidance, determine severity, and generate a customer-facing response.

The agent combines LLM reasoning with deterministic tools and an external knowledge base to provide reliable recommendations.

---

# Agent Goal

The goal of this agent is:

"Help support engineers understand customer issues, retrieve relevant troubleshooting guidance, identify severity, recommend next actions, and draft responses while reducing manual investigation time."

---

# Features

- Customer ticket analysis
- Issue classification
- Knowledge base retrieval
- Severity assessment
- Escalation decision
- Customer response generation
- Output validation
- Streamlit interface

---


---

# Tech Stack

- Python
- Ollama (llama2-uncensored)
- FastAPI
- Streamlit
- JSON Knowledge Base

---

### Run Project


Install dependencies:

```
pip install -r requirements.txt
```



### Start API:
```
uvicorn api.app:app --reload
```

### Start frontend:

```
streamlit run frontend/app.py
```

check: localhost:8501


---

# Example Input


Production job has been failing since yesterday after an API key change.


---

# Example Output

```json
{
 "summary":"Production job authentication failure",
 "issue_type":"authentication",
 "severity":"high",
 "recommended_next_steps":
 "Verify API credentials and redeploy configuration",
 "needs_escalation":true
}```
