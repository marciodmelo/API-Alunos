# schemas.py
from pydantic import BaseModel

class AlunoBase(BaseModel):
    nome: str
    cpf: str
    disciplina: str
    turma: str
    universidade: str
    cidade: str
    professora: str


class AlunoOut(AlunoBase):
    id: int

    class Config:
        orm_mode = True
