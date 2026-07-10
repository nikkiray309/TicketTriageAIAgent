import json
import ollama

from agent.models.state import AgentState
from agent.prompts import RESPONSE_GENERATION_PROMPT


class ResponseGeneratorNode:

    def __init__(self, model="llama2-uncensored"):
        self.model = model


    def run(self, state: AgentState):
        kb_context = []
        for item in state.kb_results:
            kb_context.append(
                {
                    "category": item.category,
                    "causes": item.likely_causes,
                    "fix": item.standard_fix
                }
            )


        prompt = f"""
Customer Ticket:
{state.ticket}


Knowledge Base Evidence:
{json.dumps(kb_context, indent=2)}


Severity:
{state.severity}


Escalation Required:
{state.needs_escalation}


Generate the final support response.
"""


        response = ollama.chat(
            model=self.model,
            format="json",
            messages=[
                {
                    "role": "system",
                    "content": RESPONSE_GENERATION_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        result = json.loads(
            response["message"]["content"]
        )


        state.recommended_next_steps = (
            result["recommended_next_steps"]
        )


        state.customer_response_draft = (
            result["customer_response_draft"]
        )

        return state