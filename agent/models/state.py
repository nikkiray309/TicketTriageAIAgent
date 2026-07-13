from pydantic import BaseModel, Field
from agent.models.knowledge import KnowledgeMatch
from agent.models.validation import ValidationIssue

class AgentState(BaseModel):

    ticket: str # input ticket text

    summary: str | None = None
    issue_type: str | None = None

    kb_results: list[KnowledgeMatch] = Field(default_factory=list)

    # planner agent
    should_search_kb: bool = False
    planner_reason: str | None = None


    severity: str | None = None
    severity_reason: str | None = None

    recommended_next_steps: str | None = None
    needs_escalation: bool = False
    reason_for_escalation: str | None = None

    customer_response_draft: str | None = None

    confidence: float | None = None

    supporting_evidence: list[str] = Field(default_factory=list)

    human_review_required: bool = False
    validation_issues: list[ValidationIssue] = Field(default_factory=list)
    validation_passed: bool = True