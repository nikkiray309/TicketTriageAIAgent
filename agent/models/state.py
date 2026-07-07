from pydantic import BaseModel, Field
from agent.models import KnowledgeMatch

class AgentState(BaseModel):
    """
    Shared state that flows through the entire agent workflow.
    """

    # ---------- Input ----------
    ticket: str

    # ---------- LLM Analysis ----------
    summary: str | None = None
    issue_type: str | None = None

    # ---------- Knowledge Base ----------
    # kb_results: list = Field(default_factory=list)
    kb_results: list[KnowledgeMatch] = Field(default_factory=list)
    # ---------- Decision ----------
    severity: str | None = None
    recommended_next_steps: list[str] = Field(default_factory=list)

    needs_escalation: bool = False
    reason_for_escalation: str | None = None

    # ---------- Response ----------
    customer_response_draft: str | None = None

    # ---------- Metadata ----------
    confidence: float | None = None

    supporting_evidence: list[str] = Field(default_factory=list)

    human_review_required: bool = False