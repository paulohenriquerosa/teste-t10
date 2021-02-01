from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

def verify_password(password: str, hashed_password: str):
  return password_context.verify(password, hashed_password)

def generateHash(password: str):
  return password_context.hash(password)