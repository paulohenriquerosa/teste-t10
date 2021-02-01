from typing import List
from sqlalchemy.orm import Session


from ..infra.orm.entities.debit import Debit
from ..infra.orm.repositories.debit_repository import DebitRepository

class ListDebitsService:

  def __init__(self, db: Session) -> None:
    self.db = db

  async def execute(self) -> List[Debit]:
    debitRepository = DebitRepository(self.db)
    debits = await debitRepository.findAll()
    return debits

    