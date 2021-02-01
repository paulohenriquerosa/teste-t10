from pydantic import BaseModel

from uuid import UUID

class ResponseCreateUserDTO(BaseModel):
  name: str
  email: str
  user_id: UUID