from flask import Flask, request, jsonify

app = Flask(__name__)

class Application:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None

    def register_user(self, username, password):
        if username in self.users:
            return {"message": "Error: User already exists.", "status": "error"}
        self.users[username] = password
        return {"message": "Registration successful.", "status": "success"}

    def login_user(self, username, password):
        if username not in self.users:
            return {"message": "Error: User not found.", "status": "error"}
        if self.users[username] != password:
            return {"message": "Error: Incorrect password.", "status": "error"}
        self.logged_in_user = username
        return {"message": f"Login successful. Welcome, {username}!", "status": "success"}

    def create_record(self, data):
        if not self.logged_in_user:
            return {"message": "Error: User not logged in.", "status": "error"}
        return {"message": f"Record created successfully: {data}", "status": "success"}


app_logic = Application()

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    result = app_logic.register_user(username, password)
    return jsonify(result)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    result = app_logic.login_user(username, password)
    return jsonify(result)

@app.route("/create_record", methods=["POST"])
def create_record():
    data = request.json
    record_data = data.get("data")
    result = app_logic.create_record(record_data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
