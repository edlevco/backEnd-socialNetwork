from client import Client, client_info_file
import ecrypt

class Server:
    def __init__ (self):
        self.clients = []

    def restoreClients(self):
        try:
            with open(client_info_file, 'r') as f:
                lines = f.readlines()  # Read all lines at once
        except IOError as e:
            print(f"Error opening file '{client_info_file}': {e}")
        else:
            for i in range(0, len(lines), 3):
                username = lines[i].strip()
                password = lines[i + 1].strip()
                notifications = lines[i + 2].strip()

                self.clients.append(Client(username, password, notifications, False))


    def makeNewClient(self):
        print("Creating new client\n")
        username = self.makeUsername()
        password = self.makePassword()
        notifications = 0

        newClient = Client(username, password, notifications, True)
        self.clients.append(newClient)
        newClient.writeToServer()

    def makeUsername(self):
        while True:
            unique = True
            username = input("Make a username: ")

            for client in self.clients:
                if client.username == username.lower():
                    unique = False
                    print(f"The username '{username}' already exists\nPlease enter a new username\n")
            
            if unique == True:
                break

        return username
    
    def makePassword(self):
        password = input("Enter your password: ")

        return password
    

    def findClient(self):
        username = input("Enter your username: ")

        for client in self.clients:
            if username.lower() == client.username.lower():  # Case-insensitive match
                password = input("Enter your password: ")
                print(password)
                print(ecrypt.decrypt(client.encrypt))
                if password == ecrypt.decrypt(client.encrypt):
                    print("Login successful!")
                    return client
                else:
                    return None
        password = input("Enter your password: ") # whatever they enter returns same message
        return None



        


            



            