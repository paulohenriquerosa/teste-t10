from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..infra.orm.entities.debit import Debit, DebitStatus

from ..infra.orm.repositories.debit_repository import DebitRepository

class ApproveDebitService:
  def __init__(self, db: Session) -> None:
    self.db = db

  async def execute(self, debit_id: str) -> Debit:
    debitRepository = DebitRepository(self.db)

    debit_exists = await debitRepository.findById(debit_id=debit_id)

    if (not debit_exists):
      raise HTTPException(status_code=404, detail='Debit request not found!')

    if(debit_exists.debit_status == DebitStatus.approved):
      raise HTTPException(status_code=400, detail='Automatic debit already approved!')

    debit_exists.debit_status = DebitStatus.approved

    updated_debit = await debitRepository.update(debit=debit_exists)

    return updated_debit



    