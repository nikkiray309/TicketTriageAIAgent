from agent.models.state import AgentState


class PlannerNode:
    """
    Decides which tools the agent should use.
    """


    def run(self, state: AgentState) -> AgentState:

        issue = (state.issue_type or "").lower()
        ticket = state.ticket.lower()


        # Technical troubleshooting requires KB lookup
        if issue in [
            "authentication",
            "network",
            "permissions",
            "database",
            "ssl_certificate",
            "configuration"
        ]:
            state.should_search_kb = True

            state.planner_reason = (
                "Technical issue detected. "
                "Searching knowledge base for supporting evidence."
            )


        elif any(
            word in ticket
            for word in [
                "error",
                "failed",
                "failure",
                "not working"
            ]
        ):

            state.should_search_kb = True
            state.planner_reason = (
                "Failure symptoms detected. "
                "Knowledge lookup required."
            )


        else:
            state.should_search_kb = False
            state.planner_reason = (
                "No troubleshooting information required."
            )
        return state