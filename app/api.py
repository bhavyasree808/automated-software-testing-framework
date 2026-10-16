from flask import Flask, jsonify, request

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(test_config or {})
    users = {
        1: {"id": 1, "name": "Asha", "email": "asha@example.com"},
        2: {"id": 2, "name": "Rahul", "email": "rahul@example.com"},
    }

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.get("/api/users")
    def list_users():
        return jsonify(list(users.values())), 200

    @app.get("/api/users/<int:user_id>")
    def get_user(user_id):
        user = users.get(user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user), 200

    @app.post("/api/users")
    def create_user():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON body required"}), 400
        name, email = data.get("name"), data.get("email")
        if not isinstance(name, str) or not name.strip():
            return jsonify({"error": "name is required"}), 400
        if not isinstance(email, str) or "@" not in email:
            return jsonify({"error": "valid email is required"}), 400
        next_id = max(users.keys(), default=0) + 1
        user = {"id": next_id, "name": name.strip(), "email": email.strip()}
        users[next_id] = user
        return jsonify(user), 201

    @app.delete("/api/users/<int:user_id>")
    def delete_user(user_id):
        if user_id not in users:
            return jsonify({"error": "User not found"}), 404
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200

    return app
