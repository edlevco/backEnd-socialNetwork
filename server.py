import bcrypt
import os
import json
import base64

FILE_PATH = "clients_json.json"


class Server:
    def __init__(self):
        self.initialize_json_file()

    def make_new_client(self):
        """Create a new client."""
        while True:
            username = self.make_username()
            password = self.get_password()
            hashed_pass = self.hash_password(password)

            if self.add_client(username, hashed_pass):
                print("\nSuccessful Sign Up\n")
                return self.get_client(username)
            else:
                print("Username already in use: Try Again\n")

    def make_username(self):
        """Prompt user for a unique username."""
        return input("Enter a unique username: ")

    def get_password(self):
        """Prompt user for a password."""
        return input("Enter your password: ")

    def client_login(self):
        """Log in an existing client."""
        data = self.load_json()
        username = input("Enter your username: ")

        if username in data["clients"]:
            password = input("Enter your password: ")
            stored_hash = base64.b64decode(data["clients"][username]["password"])

            if bcrypt.checkpw(password.encode(), stored_hash):
                print("Login Successful!")
                return data["clients"][username]
            else:
                print("Invalid password.")
                return None
        else:
            print("Username not found.")
            return None

    def get_client(self, username):
        """Retrieve a client by username."""
        data = self.load_json()
        return data["clients"].get(username, None)

    def hash_password(self, password):
        """Hash a password using bcrypt."""
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return base64.b64encode(hashed).decode()  # Encode in Base64 for JSON compatibility

    def add_client(self, username, password):
        """Add a new client to the JSON file."""
        data = self.load_json()

        if username in data["clients"]:
            return False

        # Add the new client
        data["clients"][username] = {
            "username": username,
            "password": password,
            "notifications": [],
            "followers": [],
            "chats": []
        }
        self.save_json(data)
        return True

    def load_json(self):
        """Load data from the JSON file."""
        with open(FILE_PATH, "r") as f:
            return json.load(f)

    def save_json(self, data):
        """Save data to the JSON file."""
        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)

    def initialize_json_file(self):
        """Create the JSON file if it doesn't exist."""
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, "w") as f:
                json.dump({"clients": {}}, f, indent=4)
