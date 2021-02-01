from sqlalchemy.orm import Session
from fastapi import HTTPException
from jose import jwt


from ..infra.orm.entities.user import User
from ..infra.orm.repositories.user_repository import UserRepository
from ..provider.hash_provider import verify_password

from  app.config.auth import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

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
      'exp': ACCESS_TOKEN_EXPIRE_MINUTES
    }
    token = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    
    return token