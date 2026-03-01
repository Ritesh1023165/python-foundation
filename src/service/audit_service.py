import logging
from datetime import datetime

logger = logging.getLogger("audit")


class AuditService:

    @staticmethod
    def log_request(request):
        logger.info(f"AUDIT_REQUEST | {datetime.utcnow()} | {request.dict()}")

    @staticmethod
    def log_response(response):
        logger.info(f"AUDIT_RESPONSE | {datetime.utcnow()} | {response}")