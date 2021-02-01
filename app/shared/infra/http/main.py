
import sys  
from pathlib import Path  
file = Path(__file__).resolve()  
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from fastapi import FastAPI

from app.shared.infra.http.routes import routes
from app.shared.infra.orm.database import Base, engine 

Base.metadata.create_all(bind=engine)

app = FastAPI()
 
app.include_router(routes)
