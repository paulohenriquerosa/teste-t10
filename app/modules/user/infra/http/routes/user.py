from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from app.shared.infra.orm.database import SessionLocal


from ....services.create_user_service import CreateUserService

from ....dtos.create_user_DTO import CreateUserDTO
from ....dtos.response_create_user_DTO import ResponseCreateUserDTO

# Dependecy 
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


user_routes = APIRouter()

@user_routes.post('', response_model=ResponseCreateUserDTO)
async def create(user_data: CreateUserDTO, db: Session = Depends(get_db)):

  # TODO: Lembrar de tirar o hash da senha
  createUserService = CreateUserService(db=db)
  new_user = await createUserService.execute(name=user_data.name, email=user_data.email, password=user_data.password)

  return new_user.__dict__


