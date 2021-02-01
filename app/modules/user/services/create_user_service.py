from sqlalchemy.orm import Session
from fastapi import HTTPException


from ..infra.orm.entities.user import User
from ..infra.orm.repositories.user_repository import UserRepository
from ..provider.hash_provider import generateHash
from app.modules.user.dtos.create_user_DTO import CreateUserDTO

class CreateUserService:
  def __init__(self, db: Session) -> None:
    self.db = db

  async def execute(self, name: str, email: str, password: str) -> User:
    userRepository = UserRepository(self.db)

    user_exists = await userRepository.findByEmail(email=email)
    if(user_exists):
      raise HTTPException(status_code=400, detail='Email already exists!')

    hashed_password = generateHash(password)
    user_data = CreateUserDTO(name=name, email=email, password=hashed_password)

    new_user = await userRepository.create(user_data)
    
    return new_user