from sqlalchemy.orm import Session

from ..entities.user import User
from ....dtos.create_user_DTO import CreateUserDTO

class UserRepository:

  def __init__(self, db: Session) -> None:
    self.db = db

  async def create(self, user: CreateUserDTO) -> User:
    new_user = User(name=user.name, email=user.email, hashed_password=user.password)
    self.db.add(new_user)
    self.db.commit()
    self.db.refresh(new_user)
    return new_user

  async def findByEmail(self, email: str) -> User:
    found_user = self.db.query(User).filter(User.email == email).first()
    return found_user

  async def findById(self, user_id:str) -> User:
    found_user = self.db.query(User).filter(User.user_id == user_id).first()
    return found_user
