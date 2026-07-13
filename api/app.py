from fastapi import FastAPI  # type: ignore[import]
from api.routes import router

app = FastAPI(
    title="Support Ticket Triage Agent API",
    version="1.0.0",
    description="AI-powered support ticket triage system."
)

@app.get("/")
def root():
    return {
        "service": "Support Ticket Triage Agent",
        "status": "running",
        "version": "1.0.0"
    }

app.include_router(router)