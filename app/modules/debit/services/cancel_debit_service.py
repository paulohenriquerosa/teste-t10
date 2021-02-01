from sqlalchemy.orm import Session
from fastapi import HTTPException


from ..infra.orm.repositories.debit_repository import DebitRepository

class CancelDebitService:
  def __init__(self, db: Session) -> None:
    self.db = db

  async def execute(self, debit_id: str) -> None:
    debitRepository = DebitRepository(self.db)

    debit_exists = await debitRepository.findById(debit_id=debit_id)

    if(not debit_exists):
      raise HTTPException(status_code=404, detail='Debit request not found')

    await debitRepository.delete(debit_id=debit_exists.debit_id)