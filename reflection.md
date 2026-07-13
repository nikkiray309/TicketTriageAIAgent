# Reflection


## 1. What problem did you choose?

I selected customer support ticket triage because support engineers spend significant time manually analyzing issues, searching documentation, and deciding severity.


## 2. How does your agent break down the task?

The agent separates the task into:

- Ticket understanding
- Planning
- Knowledge retrieval
- Severity classification
- Validation
- Response generation


## 3. What tools does your agent use?

The agent uses:

1. Knowledge base search
2. Severity classifier
3. Validation module


## 4. What worked well?

The combination of deterministic retrieval and LLM generation worked well. The knowledge base provided reliable troubleshooting information while the LLM improved response quality.


## 5. What did not work well?

Small local LLM models occasionally generated invalid JSON or incorrect issue classifications.


## 6. Where did the agent fail?

The agent struggled with:

- Very short ambiguous tickets
- Missing information on Knowledge Base


## 7. How did you evaluate output?

Evaluation was performed using manually created test cases covering:

- Successful retrieval
- Missing information
- Incorrect inputs
- Security scenarios


## 8. What guardrails were added?

Implemented:

- Output validation
- KB grounded recommendations
- Confidence checking
- Human review conditions


## 9. What would you improve?

Future improvements:

- Vector database retrieval 
- Ticket history memory (cache)
- Email Support incase of high severity


## 10. What should require human review?

Human review is required for:

- Low confidence predictions
- Production-impacting issues
- Conflicting information
- Security-sensitive requests