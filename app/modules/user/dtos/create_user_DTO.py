from pydantic import BaseModel

class CreateUserDTO(BaseModel):
  name: str
  email: str
  password: str