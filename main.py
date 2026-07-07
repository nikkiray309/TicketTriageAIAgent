from agent.workflow import run_agent


ticket = """
Customer says their production job has been failing since yesterday
after a configuration change.

They are unsure whether the issue is with authentication,
network access, or data permissions.
"""

state = run_agent(ticket)

print(state.model_dump_json(indent=4))