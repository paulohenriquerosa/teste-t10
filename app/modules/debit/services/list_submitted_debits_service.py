from typing import List
from sqlalchemy.orm import Session


from ..infra.orm.entities.debit import Debit
from ..infra.orm.repositories.debit_repository import DebitRepository

class ListSubmittedDebitsService:

  def __init__(self, db: Session) -> None:
    self.db = db

  async def execute(self) -> List[Debit]:
    debitRepository = DebitRepository(self.db)
    submitted_debits = await debitRepository.findAllSubmitteds()
    return submitted_debits

    