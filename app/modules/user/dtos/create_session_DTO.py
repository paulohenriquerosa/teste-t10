from pydantic import BaseModel

class CreateSessionDTO(BaseModel):
  email: str
  password: str