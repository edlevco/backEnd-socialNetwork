from server import Server
from termcolor import colored

server = Server()

def __main__():
    server_on = True
    self = None
    while server_on:
        joining = True
        while joining:
            print(colored("\nWelcome to PInstagram", "blue"))

            joinOption = getValidInt("\n(1) Sign up\n(2) Log in\n\n", 1, 2)
            
            if joinOption == 1:
                self = server.make_new_client()
                server.joinNotification(self["username"])
                joining = False
                break
            elif joinOption == 2:
                self = server.client_login()
                if (self != None): # if a client has been found, enter
                    joining = False

        print(colored("\nWelcome to PInstagram: "+ self["username"]+"\n", "blue"))

        isLoggedIn = True
        connected_client = None
        
        while isLoggedIn:
            newNotifications = server.get_unread(self["username"], "notifications") ## if not 0 will look like (5 new notifications): if zero will be None
            newChats = server.get_unread(self["username"], "chats")

            mainOption = getValidInt(f"\n(1) Search Accounts\n(2) View Chats {newChats}\n(3) View Notifications {newNotifications}\n{colored("(4) Sign Out", "red")}\n", 1, 4)

            if mainOption == 1:
                accountUsername = input("Search for account with username: ").capitalize()
                connected_client = server.get_client(accountUsername)
                if connected_client == None:
                    print(colored("\nNo user found with username: "+ accountUsername, "yellow"))
                else:
                    onProfile = True
                    while onProfile:
                        server.print_user_stats(self, accountUsername)
                        profileOptions = getValidInt(f"(1) Follow/ Unfollow\n(2) Send Message\n{colored("(3) Return Home", "red")}\n\n", 1, 3)

                        if profileOptions == 1:
                            server.follow_user(self, connected_client)
                        elif profileOptions == 2:
                            server.send_chat(self, connected_client)
                        elif profileOptions == 3:
                            onProfile = False
            if mainOption == 2:
                server.print_user_chats(self)
            if mainOption == 3:
                server.print_user_notifications(self)

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
                print(colored(f"Error: Please enter an integer between {min} and {max}.", "red"))
        except ValueError:
            print(colored("Error: Invalid input. Please enter a valid integer.", "red"))

__main__()

