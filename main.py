from fastapi import FastAPI
import models
from database import engine
from routers import clientes, agendamentos  # Importa nossos novos módulos

# Cria as tabelas do banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Agendamento API",
    description="API robusta e modular para gerenciamento de horários.",
    version="1.1.0"
)

# Inclui as rotas modulares na aplicação principal
app.include_router(clientes.router)
app.include_router(agendamentos.router)

@app.get("/")
def read_root():
    return {"status": "online", "mensagem": "API Modular funcionando com sucesso!"}
