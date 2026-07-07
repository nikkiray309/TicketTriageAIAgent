from agent.models.state import AgentState

def calculate_severity(ticket: str, kb_results: list):
    """
    Determine severity using KB metadata and ticket context.
    """

    ticket_lower = ticket.lower()

    severity_order = {
        "low": 1,
        "medium": 2,
        "high": 3,
        "critical": 4
    }

    severity = "low"
    reason = "No strong severity indicators found."


    # Use highest severity from retrieved KB entries

    for result in kb_results:

        kb_severity = result.severity_hint.lower()

        if severity_order.get(kb_severity, 0) > severity_order[severity]:

            severity = kb_severity

            reason = (
                f"Severity determined from knowledge base "
                f"entry {result.id} ({result.category})."
            )


    # Upgrade if production impact is mentioned

    if any(
        phrase in ticket_lower
        for phrase in [
            "production down",
            "production outage",
            "all users affected"
        ]
    ):
        severity = "critical"

        reason = (
            "Production outage indicators detected "
            "in customer ticket."
        )


    return {
        "severity": severity,
        "reason": reason
    }