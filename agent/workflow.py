from agent.state import AgentState
from agent.nodes.analyse_ticket import AnalyzeTicketNode
from tools.knowledge_search import search_knowledge_base


def run_agent(ticket: str):
    state = AgentState(ticket=ticket)
    analyze = AnalyzeTicketNode()
    state = analyze.run(state)

    state.kb_results = search_knowledge_base(
        state.ticket
    )

    return state