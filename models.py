from sqlalchemy import Column, Integer, String
from database import Base

class ClienteModel(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telefone = Column(String, nullable=False)

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
# Não apague o ClienteModel que já está aí, apenas adicione este abaixo:

class AgendamentoModel(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    data_horario = Column(DateTime, nullable=False)
    servico = Column(String, nullable=False)
    
    # A CHAVE ESTRANGEIRA: Vincula este agendamento ao ID de um cliente real
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
