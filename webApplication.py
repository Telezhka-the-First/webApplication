class Application:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None

    def register_user(self, username, password):
        if username in self.users:
            return "Error: User already exists."
        self.users[username] = password
        return "Registration successful."

    def login_user(self, username, password):
        if username not in self.users:
            return "Error: User not found."
        if self.users[username] != password:
            return "Error: Incorrect password."
        self.logged_in_user = username
        return f"Login successful. Welcome, {username}!"

    def create_record(self, data):
        if not self.logged_in_user:
            return "Error: User not logged in."
        return f"Record created successfully: {data}"


if __name__ == "__main__":
    app = Application()
    print("Welcome to the Application!")
    while True:
        print("\nChoose an action: [1] Register, [2] Login, [3] Create Record, [4] Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(app.register_user(username, password))
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(app.login_user(username, password))
        elif choice == "3":
            data = input("Enter record data: ")
            print(app.create_record(data))
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
