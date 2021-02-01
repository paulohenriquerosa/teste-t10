from fastapi.testclient import TestClient


from app.shared.infra.http.main import app


client = TestClient(app)

def test_create_user():
  response = client.post("/user", json= {
    'name': 'user1',
    'email': 'user1@gmail.com',
    'password': '123456'
  })
  assert response.status_code == 200
  assert 'name' in response.json()
  assert 'email' in response.json()
  assert 'user_id' in response.json()


def test_not_create_user_exists():
  response = client.post("/user", json= {
    'name': 'user1',
    'email': 'user1@gmail.com',
    'password': '123456'
  })
  assert response.status_code == 400
  assert response.json() == {"detail": "Email already exists!"}
  