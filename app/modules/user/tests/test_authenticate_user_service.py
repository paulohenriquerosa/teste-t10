from fastapi.testclient import TestClient


from app.shared.infra.http.main import app


client = TestClient(app)

def test_authenticate_user():
  client.post("/user", json= {
    'name': 'user2',
    'email': 'user2@gmail.com',
    'password': '123456'
  })

  response = client.post("/session", json= {
    'email': 'user2@gmail.com',
    'password': '123456'
  })
  
  assert response.status_code == 200
  assert 'token' in response.json()

def test_not_authenticate_user_with_wrong_password():

  response = client.post("/session", json= {
    'email': 'user2@gmail.com',
    'password': 'wrong-password'
  })
  
  assert response.status_code == 401
  assert response.json() == { "detail": "Incorrect email/password!"}

def test_not_authenticate_user_with_wrong_email():

  response = client.post("/session", json= {
    'email': 'wrong-email',
    'password': '123456'
  })
  
  assert response.status_code == 401
  assert response.json() == { "detail": "Incorrect email/password!"}

