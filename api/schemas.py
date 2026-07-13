from datetime import datetime
from typing import Any
from pydantic import BaseModel

class TicketRequest(BaseModel):
    ticket: str

class SuccessResponse(BaseModel):
    status: str = "success"
    timestamp: datetime
    data: Any

class ErrorResponse(BaseModel):
    status: str = "error"
    timestamp: datetime
    message: str