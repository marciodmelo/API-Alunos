# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Banco SQLite local (arquivo alunos.db na mesma pasta)
SQLALCHEMY_DATABASE_URL = "sqlite:///./alunos.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # necessário para SQLite com múltiplas threads
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependência para injetar sessão de banco em rotas (se precisar depois)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
