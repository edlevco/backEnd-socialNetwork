from client import Client, client_info_file
from server import Server

server = Server()
server.restoreClients()


def __main__():
    server_on = True
    self = None
    while server_on:
        joining = True
        while joining:
            print("Welcome to Pinstagram")

            joinOption = getValidInt("\n(1) Sign up\n(2) Log in\n", 1, 2)
            
            if joinOption == 1:
                server.makeNewClient()
                self = server.clients[-1]
                joining = False
                break
            elif joinOption == 2:
                self = server.clientLogIn()
                if (self != None): # if a client has been found, enter
                    joining = False
                else:
                    print("Incorrect username or password: Try again. \n")

        print("Welcome to Instagram: "+ self.username)

        isLoggedIn = True
        connected_client = None
        
        
        while isLoggedIn:
            mainOption = getValidInt("(1) Search Accounts\n(2) View Chats\n(3) View Notifications\n(4) Sign Out\n", 1, 4)

            if mainOption == 1:
                accountUsername = input("Search for account with username: ").lower()
                connected_client = server.getClient(accountUsername)
                if connected_client == None:
                    print("No user found with username: "+ accountUsername)
                else:
                    onProfile = True
                    while onProfile:
                        print(f"{accountUsername} \nFollowers: {len(connected_client.followers)}\n")

                        profileOptions = getValidInt("(1) Follow\n(2) Send Message\n(3) Return To Home", 1, 3)
                        if profileOptions == 1:
                            if (self.username in connected_client.followers):
                                print(f"You already follow {accountUsername}")
                            else:
                                with open("userFollowers/"+connected_client.username+".txt", "a") as f:
                                    f.write(self.username.lower())
                                print(f"You have followed: {accountUsername}")
                                connected_client.followers.append(self.username)
                        elif profileOptions == 3:
                            onProfile = False

            elif mainOption == 4:
                isLoggedIn = False


                


def getValidInt(prompt, min, max):
    while True:
        userNum = input(prompt)

        try:
            num = int(userNum)  # Attempt to parse the input as an integer

            if min <= num <= max:  # Check if the number is within range
                return num
            else:
                print(f"Error: Please enter an integer between {min} and {max}.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")


__main__()