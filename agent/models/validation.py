from pydantic import BaseModel

class ValidationIssue(BaseModel):
    code: str
    message: str
    severity: str = "warning"