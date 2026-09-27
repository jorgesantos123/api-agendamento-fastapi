import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db

# IMPORTANTE: Forçamos a importação explícita dos modelos para registrar no SQLAlchemy
from models import Base, ClienteModel, AgendamentoModel 
from main import app

# 1. Configuração de um banco de dados temporário na memória RAM para os testes
# Usamos o poolclass StaticPool para compartilhar a mesma conexão em memória entre as threads do teste
from sqlalchemy.pool import StaticPool
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. Criamos uma "Fixture" que prepara o banco antes do teste e limpa depois
@pytest.fixture(name="session")
def session_fixture():
    Base.metadata.create_all(bind=engine) # Agora ele sabe exatamente quais tabelas criar
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

# 3. Criamos o cliente de teste injetando o banco temporário no lugar do real
@pytest.fixture(name="client")
def client_fixture(session):
    def override_get_db():
        try:
            yield session
        finally:
            pass
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

# ----------------- OS TESTES -----------------

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "mensagem": "API Modular funcionando com sucesso!"}

def test_criar_cliente_sucesso(client):
    payload = {
        "nome": "Jorge Teste",
        "email": "jorge@teste.com",
        "telefone": "11999999999"
    }
    response = client.post("/clientes/", json=payload)
    assert response.status_code == 201
    
    dados = response.json()
    assert dados["nome"] == "Jorge Teste"
    assert dados["email"] == "jorge@teste.com"
    assert "id" in dados

def test_criar_cliente_email_duplicado(client):
    payload = {
        "nome": "Jorge Primeiro",
        "email": "duplicado@teste.com",
        "telefone": "11999999999"
    }
    client.post("/clientes/", json=payload)
    
    response = client.post("/clientes/", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Este e-mail já está cadastrado."
