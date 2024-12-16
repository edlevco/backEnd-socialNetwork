import ecrypt


client_info_file = "client_info.txt"

class Client:
    def __init__(self, username, password, notifications, isNew):
        password = password.lower()
        self.username = username.lower()
        if isNew:
            self.encrypt = ecrypt.encrypt(password)
        else:
            self.encrypt = password # already encrypted
        self.notifications = notifications

    def writeToServer(self):
        with open (client_info_file, "a") as f:
            f.write(self.username+"\n")
            f.write(self.encrypt+"\n")
            f.write(str(self.notifications)+"\n")

    

    



