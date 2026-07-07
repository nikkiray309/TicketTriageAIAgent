import json
import ollama

from agent.state import AgentState
from agent.prompts import SYSTEM_PROMPT


class AnalyzeTicketNode:

    def __init__(self, model="llama2-uncensored"):
        self.model = model


    def run(self, state: AgentState) -> AgentState:

        prompt = f"""
                    Analyze the following customer support ticket.
                    Return ONLY valid JSON.
                    Ticket:
                    {state.ticket}
                    
                    JSON format:
                    {{
                        "summary": "",
                        "issue_type": "",
                        "confidence": 0.0
                    }}
                """

        response = ollama.chat(
            model=self.model,
            format="json",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
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

        state.summary = result["summary"]
        state.issue_type = result["issue_type"]
        state.confidence = result["confidence"]
        return state