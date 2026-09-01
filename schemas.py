from pydantic import BaseModel, EmailStr, Field

# Esse modelo define quais dados a API espera receber quando um cliente for criado
class ClienteCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50, descripition= "Nome completo")
    email: EmailStr = Field(..., description="E-mail do clliente Válido")
    telefone: str = Field(..., description= "Telefone de contato")
# Esse modelo define o que a API vai retornar (incluindo o ID simulado)
class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str

    class Config:
        from_attibutes = True

# Esse modelo define quais dados podem ser atualizados em um cliente
class ClienteUpdate(BaseModel):
    nome: str | None = Field(None, min_length=3, max_length=50, description="Novo nome do cliente")
    email: str | None = Field(None, description="Novo e-mail do cliente")
    telefone: str | None = Field(None, description="Novo telefone de contato")

from datetime import datetime

# O que a API precisa receber para marcar um horário
class AgendamentoCreate(BaseModel):
    cliente_id: int = Field(..., description="ID do cliente que está agendando")
    data_horario: datetime = Field(..., description="Data e hora do agendamento (Ex: 2026-10-25T14:30:00)")
    servico: str = Field(..., min_length=3, max_length=100, description="Nome do serviço (Ex: Consultoria)")

# O que a API vai devolver
class AgendamentoResponse(BaseModel):
    id: int
    cliente_id: int
    data_horario: datetime
    servico: str

    class Config:
        from_attributes = True
