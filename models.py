# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    disciplina = Column(String(100), nullable=False)
    turma = Column(String(50), nullable=False)
    universidade = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    professora = Column(String(100), nullable=False)
