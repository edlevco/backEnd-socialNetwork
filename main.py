from client import Client, client_info_file
from server import Server

server = Server()
server.restoreClients()


def __main__():
    server_on = True
    current_client = None
    while server_on:
        joining = True
        while joining:
            print("Welcome to Pinstagram")

            joinOption = getValidInt("\n(1) Sign up\n(2) Log in", 1, 2)
            
            if joinOption == 1:
                server.makeNewClient()
                current_client = server.clients[-1]
                joining = False
                break
            elif joinOption == 2:
                current_client = server.findClient()
                if (current_client != None): # if a client has been found, enter
                    joining = False
                else:
                    print("Incorrect username or password: Try again. \n")

        print("Welcome to Instagram: "+ current_client.username)

        isLoggedIn = True
        connected_client = None
        
        while isLoggedIn:
            mainOption = getValidInt("(1) Search Accounts\n(2) View Chats\n(3) View Notifications", 1, 3)

            if mainOption == 1:
                accountUsername = input("Search for account with username: ").lower()
                connected_client = server.findClient(accountUsername)
                if connected_client == None:
                    print("No user found with username: "+ accountUsername)
                else:
                    print(f"Account Found: {accountUsername} \nFollowers: {connected_client.followers}")

                    profileOptions = getValidInt("(1) Follow\n(2) Send Message", 1, 2)

                    if profileOptions == 1:
                        print(f"You have followed: {accountUsername}")
                        connected_client.followers += 1


                


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