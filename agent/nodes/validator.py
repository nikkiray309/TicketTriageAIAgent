from agent.models.state import AgentState
from agent.models.validation import ValidationIssue


class ValidatorNode:

    def run(self, state: AgentState):
        issues = []

        # ----------------------------
        # Guardrail 1
        # ----------------------------

        if not state.kb_results:
            issues.append(
                ValidationIssue(
                    code="NO_KB_EVIDENCE",
                    message="No supporting KB evidence found."
                )
            )

        # ----------------------------
        # Guardrail 2
        # ----------------------------

        if state.confidence is not None:
            if state.confidence < 0.60:
                issues.append(
                    ValidationIssue(
                        code="LOW_CONFIDENCE",
                        message="LLM confidence is below threshold."
                    )
                )

        # ----------------------------
        # Guardrail 3
        # ----------------------------

        if state.severity == "critical":
            issues.append(
                ValidationIssue(
                    code="CRITICAL_ISSUE",
                    message="Critical issues require human approval."
                )
            )

        # ----------------------------
        # Guardrail 4
        # ----------------------------

        if not state.customer_response_draft:
            issues.append(
                ValidationIssue(
                    code="NO_CUSTOMER_RESPONSE",
                    message="Customer response was not generated."
                )
            )

        # ----------------------------
        # Final decision
        # ----------------------------

        if issues:
            state.validation_passed = False
            state.validation_issues = issues
            state.human_review_required = True

        else:
            state.validation_passed = True
        return state