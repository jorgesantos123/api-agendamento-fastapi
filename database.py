from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# O SQLite cria um arquivo local chamado 'agendamentos.db' automaticamente
SQLALCHEMY_DATABASE_URL = "sqlite:///./agendamentos.db"

# Conecta o Python ao banco de dados
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria o criador de sessões (para abrir e fechar transações com o banco)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe mãe que gerencia e mapeia nossas tabelas
Base = declarative_base()

# Função utilitária (Dependency Injection) para gerenciar o ciclo de vida da conexão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
