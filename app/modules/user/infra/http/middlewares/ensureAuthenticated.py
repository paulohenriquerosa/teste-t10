
from jose import jwt
from typing import Optional
from fastapi import HTTPException, Header
from jose.exceptions import JWTError

from  app.config.auth import SECRET_KEY, ALGORITHM

async def ensureAuthenticated(authorization: Optional[str]= Header(None)):
  
  if not authorization:
    raise HTTPException(status_code=400, detail='Token is missing!')

  token = authorization.split(" ")[1]

  try:
    
    jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

  except JWTError as error:
    print(error)
    raise HTTPException( status_code = 401, detail= "Unauthorized")
