from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm.session import Session
from app.shared.infra.orm.database import SessionLocal

from ....services.list_debits_service import ListDebitsService
from ....services.create_debit_service import CreateDebitService
from ....services.cancel_debit_service import CancelDebitService
from ....services.approve_debit_service import ApproveDebitService
from ....services.reject_debit_service import RejectDebitService
from ....services.list_submitted_debits_service import ListSubmittedDebitsService
from ....services.submitted_debit_service import SubmittedDebitService


from ....dtos.createDebitDTO import CreateDebitDTO

debit_routes = APIRouter()


# Dependecy
def get_db(): 
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()



@debit_routes.get('/')
async def index(db: Session = Depends(get_db)):
  listDebitsService = ListDebitsService(db=db)
  debits = await listDebitsService.execute()
  return debits


@debit_routes.post('/')
async def create( data: CreateDebitDTO, db: Session = Depends(get_db)):
  createDebitService = CreateDebitService(db=db)
  debit = await createDebitService.execute(data=data)
  return debit.__dict__


@debit_routes.delete('/{debit_id}')
async def cancel(debit_id: str, db: Session = Depends(get_db)):
  cancelDebitService = CancelDebitService(db=db)
  await cancelDebitService.execute(debit_id=debit_id)
  return {"message":"Automatic debit canceled!"}


@debit_routes.put('/approve/{debit_id}')
async def approve(debit_id: str, db: Session = Depends(get_db)):
  approveDebitService = ApproveDebitService(db=db)
  updated_debit = await approveDebitService.execute(debit_id=debit_id)
  return updated_debit.__dict__

@debit_routes.put('/reject/{debit_id}')
async def reject(debit_id: str , db: Session = Depends(get_db)):
  rejectDebitService = RejectDebitService(db=db)
  updated_debit = await rejectDebitService.execute(debit_id=debit_id)
  return updated_debit.__dict__

@debit_routes.get('/submitted')
async def index_submitteds(db: Session = Depends(get_db)):
  listSubmittedDebitsService = ListSubmittedDebitsService(db=db)
  submitted_debits = await listSubmittedDebitsService.execute()
  return submitted_debits

@debit_routes.get('/submitted/{debit_id}')
async def show_submitted(debit_id: str , db: Session = Depends(get_db)):
  submittedDebitService = SubmittedDebitService(db=db)
  submitted_debit = await submittedDebitService.execute(debit_id=debit_id)
  return submitted_debit.__dict__
