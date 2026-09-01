from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import get_db
from schemas import ClienteCreate, ClienteResponse, ClienteUpdate

# O APIRouter agrupa as rotas e adiciona um prefixo automático (/clientes)
router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=ClienteResponse, status_code=201)  # Note que agora usamos @router e apenas "/"
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    cliente_existente = db.query(models.ClienteModel).filter(models.ClienteModel.email == cliente.email).first()
    if cliente_existente:
        raise HTTPException(status_code=400, detail="Este e-mail já está cadastrado.")
    
    novo_cliente = models.ClienteModel(nome=cliente.nome, email=cliente.email, telefone=cliente.telefone)
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente

@router.get("/", response_model=list[ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(models.ClienteModel).all()

@router.put("/{cliente_id}", response_model=ClienteResponse)
def atualizar_cliente(cliente_id: int, dados_novos: ClienteUpdate, db: Session = Depends(get_db)):
    cliente = db.query(models.ClienteModel).filter(models.ClienteModel.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    
    dados_para_atualizar = dados_novos.model_dump(exclude_unset=True)
    for chave, valor in dados_para_atualizar.items():
        setattr(cliente, chave, valor)
    
    db.commit()
    db.refresh(cliente)
    return cliente

@router.delete("/{cliente_id}", status_code=204)
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(models.ClienteModel).filter(models.ClienteModel.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    db.delete(cliente)
    db.commit()
    return None
