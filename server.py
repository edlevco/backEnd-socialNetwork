import bcrypt
import os
import json
import base64
from termcolor import colored

FILE_PATH = "clients_json.json"

class Server:
    
    def __init__(self):
        self.initialize_json_file() # make the json file when server is made
        
    def make_new_client(self):
        """Create a new client."""
        while True:
            username = self.make_username()
            password = self.get_password()
            hashed_pass = self.hash_password(password)

            if self.add_client(username, hashed_pass):
                print(colored("\nSign Up Successful!\n", "green"))
                return self.get_client(username)
            else:
                print(colored("Username already in use: Try Again\n", "yellow"))

    def make_username(self):
        """Prompt user for a unique username."""
        return input("Enter a unique username: ").capitalize()

    def get_password(self):
        """Prompt user for a password."""
        return input("Enter your password: ")

    def client_login(self):
        """Log in an existing client."""
        data = self.load_json()
        username = input("Enter your username: ").capitalize()


        if username in data["clients"]:
            password = input("Enter your password: ")
            stored_hash = base64.b64decode(data["clients"][username]["password"])

            if bcrypt.checkpw(password.encode(), stored_hash):
                print(colored("Login Successful!", "green"))
                return data["clients"][username]
            else:
                print(colored("\nInvalid password.", "red"))
                return None
        else:
            print(colored("\nUsername not found.", "red"))
            return None

    def get_client(self, username):
        """Retrieve a client by username."""
        data = self.load_json()
        return data["clients"].get(username.capitalize(), None)

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
        return True ## use has been made and added to JSON file

    def load_json(self):
        # read JSON and return its contents
        with open(FILE_PATH, "r") as f:
            return json.load(f)

    def save_json(self, data):
        # dump the data back in with an indent of 4
        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)

    def initialize_json_file(self):
        """Create the JSON file if it doesn't exist."""
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, "w") as f:
                json.dump({"clients": {}}, f, indent=4)

            ## make Pinstagram acount
            populated_array = self.make_array(9)
            data = self.load_json()
            data["clients"]["Pinstagram"] = {
                "username": "Pinstagram",
                "password": self.hash_password("weoifjwoifjoijoijoijoij"),
                "followers": populated_array,
                "notifications": [],
                "chats": []
            }
            self.save_json(data)
                
    
    def follow_user(self, follower_username, followed_username):
        data = self.load_json()
        follower = data["clients"].get(follower_username)
        followed = data["clients"].get(followed_username)

        if follower_username == followed_username:
            print(colored("You cannot follow yourself", "yellow"))
        elif follower_username in followed["followers"]:
            print(colored(f"\nYou have unfollowed {followed["username"]}", "blue"))
            followed["notifications"].append({"message": f"{follower["username"]} has unfollowed you.", "isRead": False})
            followed["followers"].remove(follower["username"])
        else:
            followed["notifications"].append({"message": f"{follower_username} has followed you.", "isRead": False})
            followed["followers"].append(follower_username)
            print(colored(f"\nYou have followed {followed_username}", "green"))
        self.save_json(data)
    
    def send_chat(self, sender_username, recipient_username):
        data = self.load_json()
        sender = data["clients"].get(sender_username)
        recipient = data["clients"].get(recipient_username)

        message = input(f"To {recipient_username}:\n{sender_username}: ")
        recipient["notifications"].append({"message": f"{sender_username} has sent you a message.", "isRead": False})
        recipient["chats"].append({"from": sender_username, "message": message, "isRead": False})
        self.save_json(data)

        print(colored(f"\nMessage sent to {recipient_username}", "green"))

    def print_user_stats(self, current, username):
        data = self.load_json()
        followers = data["clients"].get(username)["followers"]
        follow_status = None
        if current["username"] in followers:
            follow_status = colored("Following", "green")
        else:
            follow_status = colored("Follow", "blue")

        print(f"\nAccount: {username}\nFollowers: {len(data["clients"][username]["followers"])}\n{follow_status}\n")

    def get_unread(self, username, category):
        unread_count = 0
        data = self.load_json()
        user = data["clients"].get(username)

        for thing in user[category]:
            if thing["isRead"] == False:
                unread_count += 1
        
        if unread_count == 0: ## if they have no new notifications return nothing
            return ""
        else: ## if they have a new notification return a string to display
            return colored(f"({unread_count} new {category})", "blue")
    
    def print_user_category(self, user, category):
        data = self.load_json()
        username = user["username"]
        user = data["clients"].get(username)
        ## category could either be chats or notifications
        if user[category] == []:
            print(colored(f"\nYou have 0 {category}", "yellow"))
        else:
            print(f"\n{username}'s {category}\n")
            for thing in user[category]:
                if thing["isRead"]:
                    if category == "notifications":
                        print(thing["message"])
                    else:
                        print(f"{thing["from"]}: {thing["message"]}")
                else:
                    if category == "notifications":
                        print(colored(f"NEW: {thing["message"]} ", "blue"))
                    else:
                        print(colored(f"{thing["from"]}: {thing["message"]} (NEW)", "blue"))

                    thing["isRead"] = True
        
        self.save_json(data)

    def joinNotification(self, username):
        data = self.load_json()
        user = data["clients"].get(username)

        user["notifications"].append({"message": "PInstagram has sent you a message.", "isRead": False})
        user["chats"].append({"from": "PInstagram", "message": "Welcome to PInstagram!!", "isRead": False})

        self.save_json(data)
    
    def make_array(self, size):
        return ["filler_user" for a in range(size)]


    
