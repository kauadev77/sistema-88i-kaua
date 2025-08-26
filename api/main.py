# Este arquivo é o entry point da API FastAPI.
# Define os endpoints para sinistros.

from fastapi import FastAPI, HTTPException
from typing import Dict
from uuid import uuid4
from .models import SinistroCreate
from .database import get_db, create_sinistro, get_sinistro, get_sinistro_relatorio

app = FastAPI()

@app.post("/sinistros", response_model=Dict)
def submit_sinistro(sinistro: SinistroCreate):
    db = get_db()
    id_sinistro = str(uuid4())
    create_sinistro(db, id_sinistro, sinistro.dict())
    return {"id": id_sinistro, "status": "EM_ANALISE"}

@app.get("/sinistros/{id}")
def get_status(id: str):
    db = get_db()
    sinistro = get_sinistro(db, id)
    if not sinistro:
        raise HTTPException(404, "Não encontrado")
    return {"status": "EM_ANALISE"}

@app.get("/sinistros/{id}/relatorio")
def get_relatorio(id: str):
    db = get_db()
    relatorio = get_sinistro_relatorio(db, id)
    if not relatorio:
        raise HTTPException(404, "Não encontrado")
    return {"relatorio": {"decisao": "APROVAR"}}

@app.get("/health")
def health_check():
    return {"status": "OK"}
