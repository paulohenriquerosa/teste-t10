
from pydantic import BaseModel

from uuid import UUID

class ResponseDebitDTO(BaseModel):
  debit_status: str
  company: str
  user_id: UUID