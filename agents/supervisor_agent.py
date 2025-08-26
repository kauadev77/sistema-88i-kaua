# Este arquivo implementa o SupervisorAgent.
# Ele orquestra os outros agentes e toma decisão final.

from typing import Dict, Any
from .base import BaseAgent
from .document_agent import DocumentAnalysisAgent
from .fraud_agent import FraudDetectionAgent

class SupervisorAgent(BaseAgent):
    """Agente supervisor para coordenação.

    Orquestra análise e decide o resultado.

    TODO: Integrar com LangGraph para fluxo otimizado.
    TODO: Gerenciar estado compartilhado.
    """

    def __init__(self):
        super().__init__()
        self.document_agent = DocumentAnalysisAgent()
        self.fraud_agent = FraudDetectionAgent()

    async def supervise(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Supervisiona o processo completo.

        Args:
            state: Estado inicial do sinistro.

        Returns:
            Estado com decisão final.

        TODO: Aplicar regras complexas: aprovar se score < 0.3, investigar > 0.7, negar > 0.8.
        TODO: Adicionar lógica de decisão consistente.
        """
        # Simulação de orquestração
        state = await self.document_agent.analyze_document(state)
        state = await self.fraud_agent.detect_fraud(state)

        # Decisão simples baseada em score
        if state.get('score_fraude', 0) < 0.3:
            state['decisao_final'] = 'APROVAR'
        elif state.get('score_fraude', 0) > 0.8:
            state['decisao_final'] = 'NEGAR'
        else:
            state['decisao_final'] = 'INVESTIGAR'

        return state
