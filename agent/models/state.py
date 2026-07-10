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
    recommended_next_steps: list[str] = Field(default_factory=list)

    needs_escalation: bool = False
    reason_for_escalation: str | None = None

    customer_response_draft: str | None = None

    confidence: float | None = None

    supporting_evidence: list[str] = Field(default_factory=list)

    human_review_required: bool = False

    #Guardrails
    validation_issues: list[ValidationIssue] = Field(default_factory=list)
    validation_passed: bool = True

    
# class AgentState(BaseModel):
#     """
#     Shared state that flows through the entire agent workflow.
#     """

#     # ---------- Input ----------
#     ticket: str

#     # ---------- LLM Analysis ----------
#     summary: str | None = None
#     issue_type: str | None = None

#     # ---------- Knowledge Base ----------
#     # kb_results: list = Field(default_factory=list)
#     kb_results: list[KnowledgeMatch] = Field(default_factory=list)
#     # ---------- Decision ----------
#     severity: str | None = None
#     recommended_next_steps: list[str] = Field(default_factory=list)

#     needs_escalation: bool = False
#     reason_for_escalation: str | None = None

#     # ---------- Response ----------
#     customer_response_draft: str | None = None

#     # ---------- Metadata ----------
#     confidence: float | None = None

#     supporting_evidence: list[str] = Field(default_factory=list)

#     human_review_required: bool = False