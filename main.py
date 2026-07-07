import ollama


ticket = """
Customer says their production job has been failing since yesterday 
after a configuration change.

They are unsure whether the issue is with authentication,
network access, or data permissions.
"""


prompt = f"""
You are a customer support triage assistant.

Analyze this support ticket.

Return ONLY JSON.

Ticket:

{ticket}

Output format:

{{
    "summary": "",
    "issue_type": "",
    "severity": ""
}}
"""

response = ollama.chat(
    model="llama2-uncensored",
    format="json",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)


print(response["message"]["content"])