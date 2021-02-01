
from typing import List
from sqlalchemy.orm import Session

from..entities.debit import Debit, DebitStatus


from ....dtos.createDebitDTO import CreateDebitDTO

class DebitRepository:
  def __init__(self, db: Session) -> None:
    self.db = db

  async def findAll(self) -> List[Debit]:
    debits = self.db.query(Debit).all()
    return debits

  async def findByName(self, company_name) -> Debit or None:
    debit = self.db.query(Debit).filter(Debit.company == company_name).first()
    return debit

  async def findById(self, debit_id: str) -> Debit or None:
    debit = self.db.query(Debit).filter(Debit.debit_id == debit_id).first()
    return debit

  async def findAllSubmitteds(self) -> List[Debit]:
    submitted_debits = self.db.query(Debit).filter(Debit.debit_status == DebitStatus.submitted).all()
    return submitted_debits

  async def findSubmitted(self, debit_id: str) -> Debit or None:
    submitted_debit = self.db.query(Debit).filter(Debit.debit_id == debit_id, Debit.debit_status == DebitStatus.submitted).first()
    return submitted_debit

  async def create(self, data: CreateDebitDTO) -> Debit:
    debit = Debit(debit_status=DebitStatus.submitted, **data.dict())
    self.db.add(debit)
    self.db.commit()
    self.db.refresh(debit)
    return debit

  async def delete(self, debit_id: str) -> None:
    self.db.query(Debit).filter(Debit.debit_id == debit_id).delete()
    self.db.commit()
    
  async def update(self, debit:Debit) -> Debit:    
    self.db.query(Debit).filter(Debit.debit_id == debit.debit_id).update({Debit.debit_status: debit.debit_status})
    self.db.commit()
    self.db.refresh(debit)
    return debit
