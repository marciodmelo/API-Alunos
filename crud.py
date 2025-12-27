# crud.py
from sqlalchemy.orm import Session
import models

def listar_alunos(db: Session):
    return db.query(models.Aluno).all()
