import uuid
from fastapi import Request

async def add_correlation_id(request: Request, call_next):
    correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
    # Store it in the request state
    request.state.correlation_id = correlation_id
    response = await call_next(request)
    response.headers["X-Correlation-ID"] = request.state.correlation_id
    return response

def get_cid(request: Request):
    return getattr(request.state, "correlation_id", None)