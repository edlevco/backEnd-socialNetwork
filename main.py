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
            joinOption = input("""Welcome to Instagram!
                
                (1) Log In
                (2) Sign up
                            
                """)
            
            if joinOption == "2":
                server.makeNewClient()
                current_client = server.clients[-1]
                joining = False
                break
            elif joinOption == "1":
                current_client = server.findClient()
                if (current_client != None): # if a client has been found, enter
                    joining = False
                else:
                    print("Incorrect username or password: Try again. \n")
            else:
                print("Please enter a valid option: (1) or (2)")

        print("Welcome to Instagram: "+ current_client.username)


            

        

        
        


            


        

    











__main__()