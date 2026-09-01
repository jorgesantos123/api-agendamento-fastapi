from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import get_db
from schemas import AgendamentoCreate, AgendamentoResponse

router = APIRouter(prefix="/agendamentos", tags=["Agendamentos"])

@router.post("/", response_model=AgendamentoResponse, status_code=201)
def criar_agendamento(agendamento: AgendamentoCreate, db: Session = Depends(get_db)):
    cliente = db.query(models.ClienteModel).filter(models.ClienteModel.id == agendamento.cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Não é possível agendar: Cliente não encontrado.")
    
    novo_agendamento = models.AgendamentoModel(
        cliente_id=agendamento.cliente_id,
        data_horario=agendamento.data_horario,
        servico=agendamento.servico
    )
    db.add(novo_agendamento)
    db.commit()
    db.refresh(novo_agendamento)
    return novo_agendamento

@router.get("/", response_model=list[AgendamentoResponse])
def listar_agendamentos(db: Session = Depends(get_db)):
    return db.query(models.AgendamentoModel).all()
