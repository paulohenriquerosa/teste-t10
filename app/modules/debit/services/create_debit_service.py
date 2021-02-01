from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..infra.orm.repositories.debit_repository import DebitRepository

from ..infra.orm.entities.debit import Debit

from ..dtos.createDebitDTO import CreateDebitDTO

class CreateDebitService:
  def __init__(self, db: Session) -> None:
    self.db = db

  async def execute(self, data: CreateDebitDTO ) -> Debit:
    debitRepository = DebitRepository(self.db)

    debit_exists = await debitRepository.findByName(data.company)
    if (debit_exists):
      raise HTTPException(status_code=400, detail='Automatic debit already submitted!')

    debit = await debitRepository.create(data=data)

    return debit
