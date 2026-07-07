from agent.workflow import run_agent


ticket = """
Customer says their production job has been a failure since yesterday after a configuration change.
"""

state = run_agent(ticket)

print(state.model_dump_json(indent=4))