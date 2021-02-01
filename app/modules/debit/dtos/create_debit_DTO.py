
from pydantic import BaseModel

class CreateDebitDTO(BaseModel):
  company: str