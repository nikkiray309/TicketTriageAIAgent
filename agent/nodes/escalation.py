from agent.models.state import AgentState


class EscalationNode:
    """
    Determines whether human escalation is required.
    """


    def run(self, state: AgentState) -> AgentState:

        severity = (
            state.severity.lower()
            if state.severity
            else "low"
        )


        if severity == "critical":

            state.needs_escalation = True

            state.reason_for_escalation = (
                "Critical severity detected. "
                "Immediate human intervention required."
            )


        elif severity == "high":

            state.needs_escalation = True

            state.reason_for_escalation = (
                "High severity technical issue. "
                "Support engineer review recommended."
            )


        else:

            state.needs_escalation = False

            state.reason_for_escalation = (
                "Issue can be handled automatically."
            )


        return state