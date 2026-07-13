from datetime import datetime
from fastapi import APIRouter, HTTPException
from api.services import build_ticket_response
from api.schemas import (
    TicketRequest,
    SuccessResponse,
    ErrorResponse,
)
from agent.workflow import run_agent

# version 1.0.0
router = APIRouter(
    prefix="/api/v1",
    tags=["Ticket Analysis"]
)

@router.post(
    "/analyze",
    response_model=SuccessResponse,
    responses={
        500: {"model": ErrorResponse}
    }
)

def analyze_ticket(request: TicketRequest):
    try:
        state = run_agent(request.ticket)
        response_data = build_ticket_response(state)
        
        return SuccessResponse(
            timestamp=datetime.utcnow(),
            data=response_data
)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )