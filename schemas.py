from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

# MODELO DE CRIAÇÃO DE CLIENTE
class ClienteCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50, description="Nome completo") # Corrigido 'description'
    email: str = Field(..., description="E-mail do cliente")
    telefone: str = Field(..., description="Telefone de contato")

# MODELO DE RETORNO DE CLIENTE
class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str

    # Corrigido: Forma moderna de habilitar a conversão com o ORM (SQLAlchemy)
    model_config = ConfigDict(from_attributes=True)

# MODELO DE ATUALIZAÇÃO DE CLIENTE
class ClienteUpdate(BaseModel):
    nome: str | None = Field(None, min_length=3, max_length=50, description="Novo nome do cliente")
    email: str | None = Field(None, description="Novo e-mail do cliente")
    telefone: str | None = Field(None, description="Novo telefone de contato")

# MODELO DE CRIAÇÃO DE AGENDAMENTO
class AgendamentoCreate(BaseModel):
    cliente_id: int = Field(..., description="ID do cliente")
    data_horario: datetime = Field(..., description="Data e hora (Ex: 2026-10-25T14:30:00)")
    servico: str = Field(..., min_length=3, max_length=100, description="Nome do serviço")

# MODELO DE RETORNO DE AGENDAMENTO
class AgendamentoResponse(BaseModel):
    id: int
    cliente_id: int
    data_horario: datetime
    servico: str

    # Corrigido: Forma moderna de habilitar a conversão com o ORM
    model_config = ConfigDict(from_attributes=True)
