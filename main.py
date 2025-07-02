'''
THis is the programs starting point, every .py process will be dependent on the main.py start

Main.py contains a basic text-based UX, guiding the user to either the server or client functionality of the program
'''

import threading
from servers.server import Server
from clients.client_ui import client_mode

def main():
    while True:
        mode_select = input(
            ">_ Mode selection. Please select on of the displayed modes:\n"
            "  [1] Initiate server \n"
            "  [2] Client mode \n"
            "  [(e)xit] End process \n"
            "User input > "
        ).strip()


        '''call to the server functionality, takes input the input for server.py to use in AF_INET connection,
        whihc requires ip and an open port'''
        if mode_select == '1':
            print('\n>_ Server selected.')

            ip_input = input(">_ Enter IPv4 to bind server (default 0.0.0.0): ") or "0.0.0.0"
            if ip_input.lower() in ['e', 'exit']:
                break

            port_input = input(">_ Enter open port to listen on: ")
            if port_input.lower() in ['e', 'exit']:
                break

            try:
                port = int(port_input)
            except ValueError:
                print(">_ [!] Invalid port. Please, try again. [!] <")
                continue

            server = Server(ip_input, port)
            threading.Thread(target=server.start).start()


            '''Call to the client functionaity'''
        elif mode_select == '2':
            client_mode()


            # program exit
        elif mode_select.lower() in ['e', 'exit']:
            print('>_ Exiting program... <')
            break


            # error handling
        else:
            print('>_ [!] Invalid input. Please, try again. [!] <\n')


if __name__ == "__main__":
    main()