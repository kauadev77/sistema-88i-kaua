# Sistema de Análise de Sinistros - 88i Kaua

Este é um protótipo simples (cerca de 40% completo) para o teste técnico da Olga AI.
É um sistema para analisar sinistros usando agentes LangGraph, workflows Kestra, API FastAPI e banco PostgreSQL.

## Instruções de Instalação

1. Clone o repositório.
2. Crie um ambiente virtual: python -m venv venv
3. Ative: source venv/bin/activate (Linux/Mac) ou venv\Scripts\activate (Windows)
4. Instale dependências: pip install -r requirements.txt
5. Rode o Docker: docker-compose up -d
6. Rode a API: uvicorn api.main:app --reload

## Uso

- Envie um sinistro via POST /sinistros
- Consulte status via GET /sinistros/{id}

TODO: Adicionar mais detalhes na documentação.
"# sistema-88i-kaua" 
