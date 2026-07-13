from agent.models.state import AgentState


def build_ticket_response(state: AgentState):
    """
    Converts internal agent state
    into frontend-friendly response.
    """

    return {

        "summary": state.summary,

        "issue_type": state.issue_type,

        "severity": state.severity,

        "severity_reason": state.severity_reason,

        "recommended_next_steps":
            state.recommended_next_steps,

        "needs_escalation":
            state.needs_escalation,

        "reason_for_escalation":
            state.reason_for_escalation,

        "customer_response_draft":
            state.customer_response_draft,


        "validation": {
            "passed":
                state.validation_passed,
            "issues":
                [
                    issue.model_dump()
                    for issue in state.validation_issues
                ]
        }
    }