from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:docker@localhost:5432/t10_database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

if not database_exists(engine.url):
  create_database(engine.url)
  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()