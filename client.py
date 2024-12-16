import bcrypt


client_info_file = "client_info.txt"

class Client:
    def __init__(self, username, password, notifications, isNew):
        password = password.lower()
        self.username = username.lower()
        if isNew:
            self.hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        else:
            self.hashed = password # already hashed 
        self.notifications = notifications

    def writeToServer(self):
        with open (client_info_file, "a") as f:
            f.write(self.username+"\n")
            f.write(str(self.hashed)+"\n")
            f.write(str(self.notifications)+"\n")

    

    



