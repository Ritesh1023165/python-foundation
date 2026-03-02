from src.service.risk_engine import RiskEngine
from src.service.orchestrator import RiskOrchestrator



def get_risk_engine():
    return RiskEngine()

def get_risk_orchestrator():
    return RiskOrchestrator()