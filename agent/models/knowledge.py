from pydantic import BaseModel


class KnowledgeMatch(BaseModel):
    id: str
    category: str
    score: int
    matched_keywords: list[str]
    likely_causes: list[str]
    standard_fix: str
    severity_hint: str
    base_confidence: float