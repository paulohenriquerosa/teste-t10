from datetime import datetime
from uuid import uuid4

from sqlalchemy import  Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.shared.infra.orm.database import Base

class User(Base):

  __tablename__ = 'users'

  user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, index=True)
  name = Column(String, index=True)
  email = Column(String, unique=True, index=True )
  hashed_password = Column(String)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


