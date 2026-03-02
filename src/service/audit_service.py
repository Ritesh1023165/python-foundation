import logging
from datetime import datetime
from fastapi import Response, Request

logger = logging.getLogger("audit")


class AuditService:

    @staticmethod
    def log_request(request, correlation_id):
        logger.info(f"AUDIT_REQUEST | Correlation-ID: {correlation_id} | {datetime.utcnow()} | {request.dict()}")

    @staticmethod
    def log_response(response, correlation_id):
        logger.info(f"AUDIT_RESPONSE | Correlation-ID: {correlation_id} | {datetime.utcnow()} | {response}")