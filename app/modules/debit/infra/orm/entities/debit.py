
from uuid import uuid4
from datetime import datetime
import enum

from sqlalchemy import  Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID

from app.shared.infra.orm.database import  Base


class DebitStatus(str, enum.Enum):
  approved = 'Approved'
  submitted = 'Submitted'
  cancelled = 'Cancelled'
  rejected = 'Rejected'

class Debit(Base):

  __tablename__ = 'debits'

  debit_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, index=True)
  debit_status = Column(Enum(DebitStatus))
  company = Column(String, index=True)
  created_at = Column(DateTime(), default=datetime.now())
  updated_at = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())