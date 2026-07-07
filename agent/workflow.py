from agent.nodes.analyse_ticket import AnalyzeTicketNode
from agent.models.state import AgentState
from agent.nodes.planner import PlannerNode
from agent.nodes.escalation import EscalationNode
from tools.knowledge_search import search_knowledge_base
from tools.severity import calculate_severity

def run_agent(ticket: str):

    state = AgentState(ticket=ticket)


    # Node 1
    state = AnalyzeTicketNode().run(state)


    # Node 2
    state = PlannerNode().run(state)


    # Tool call decision
    if state.should_search_kb:

        state.kb_results = search_knowledge_base(
            state.ticket
        )
        severity_result = calculate_severity(
        state.ticket,
        state.kb_results
    )

        state.severity = severity_result["severity"]
        state.severity_reason = severity_result["reason"]
        state = EscalationNode().run(state)

    return state