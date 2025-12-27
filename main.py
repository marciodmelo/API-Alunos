from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import models
from schemas import AlunoOut
import crud

# Criar tabela
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bem-vindo a disciplina de Arquitetura e Desenvolvimento de APIs",
    version="1.0.0",
    description="Aluno: Márcio Melo - RU: 4608448"
)

# Ver Tabela
@app.get("/alunos", response_model=list[AlunoOut])
def listar_alunos(db: Session = Depends(get_db)):
    return crud.listar_alunos(db)
