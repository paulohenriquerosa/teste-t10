from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm.session import Session
from app.shared.infra.orm.database import SessionLocal


from ....services.authenticate_user_service import AuthenticateUserService


class UserData(BaseModel):
  email: str
  password: str


# Dependecy 
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


session_routes = APIRouter()

@session_routes.post('/')
async def create(user_data: UserData, db: Session = Depends(get_db)):

  authenticateUserService = AuthenticateUserService(db=db)
  token = await authenticateUserService.execute(email=user_data.email, password=user_data.password)

  return {'token':token}


