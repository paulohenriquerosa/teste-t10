from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException


from ..infra.orm.entities.debit import Debit
from ..infra.orm.repositories.debit_repository import DebitRepository

class SubmittedDebitService:

  def __init__(self, db: Session) -> None:
    self.db = db

  async def execute(self, debit_id: str) -> List[Debit]:
    debitRepository = DebitRepository(self.db)
    submitted_debit = await debitRepository.findSubmitted(debit_id=debit_id)

    if (not submitted_debit):
      raise HTTPException(status_code=404, detail='Automatic debit not found!')

    return submitted_debit
