# Este arquivo define a classe base para todos os agentes LangGraph.
# Ele ajuda a compartilhar código comum, como o estado do sinistro.

from typing import Dict, Any

class BaseAgent:
    """Classe base para agentes.

    TODO: Integrar com LangGraph real para grafos e estados.
    """

    def __init__(self):
        # Inicializa configurações comuns
        pass  # TODO: Configurar LLM como OpenAI aqui

    async def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Método base para executar o agente.

        Args:
            state: Estado atual do sinistro.

        Returns:
            Estado atualizado.

        TODO: Adicionar lógica de estado compartilhado com Redis ou similar.
        """
        return state
