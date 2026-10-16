def test_list_users_returns_seed_users(client):
    response = client.get("/api/users")
    assert response.status_code == 200
    users = response.get_json()
    assert len(users) == 2
    assert {"id", "name", "email"} <= users[0].keys()

def test_get_existing_user(client):
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert response.get_json()["email"] == "asha@example.com"

def test_get_missing_user_returns_404(client):
    response = client.get("/api/users/999")
    assert response.status_code == 404
    assert response.get_json()["error"] == "User not found"

def test_create_user_returns_201(client):
    response = client.post("/api/users", json={"name": "Bhavya", "email": "bhavya@example.com"})
    assert response.status_code == 201
    assert response.get_json()["name"] == "Bhavya"

def test_create_user_rejects_missing_name(client):
    response = client.post("/api/users", json={"email": "test@example.com"})
    assert response.status_code == 400
    assert response.get_json()["error"] == "name is required"

def test_create_user_rejects_invalid_email(client):
    response = client.post("/api/users", json={"name": "Test", "email": "invalid"})
    assert response.status_code == 400
    assert response.get_json()["error"] == "valid email is required"

def test_delete_user(client):
    response = client.delete("/api/users/1")
    assert response.status_code == 200
    assert client.get("/api/users/1").status_code == 404

def test_delete_missing_user_returns_404(client):
    response = client.delete("/api/users/999")
    assert response.status_code == 404
