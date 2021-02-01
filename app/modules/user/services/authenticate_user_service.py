from sqlalchemy.orm import Session
from fastapi import HTTPException
from jose import jwt


from ..infra.orm.repositories.user_repository import UserRepository
from ..provider.hash_provider import verify_password

from ..dtos.create_session_DTO import CreateSessionDTO

from  app.config.auth import SECRET_KEY, ALGORITHM

class AuthenticateUserService:
  def __init__(self, db: Session) -> None:
    self.db = db

  async def execute(self, email: str, password: str) -> str:
    userRepository = UserRepository(self.db)

    user_exists = await userRepository.findByEmail(email=email)

    if(not user_exists):
      raise HTTPException(status_code=401, detail='Incorrect email/password!')

    password_match = verify_password(password=password, hashed_password=user_exists.hashed_password)

    if(not password_match):
      raise HTTPException(status_code=401, detail='Incorrect email/password!')


    to_encode = {
      'user_id' : user_exists.user_id.hex,
    }
    token = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    
    return token