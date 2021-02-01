from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker


from app.config.database import USERNAME, PASSWORD, HOST, PORT,DATA_BASE_NAME

SQLALCHEMY_DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATA_BASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

if not database_exists(engine.url):
  create_database(engine.url)
  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()