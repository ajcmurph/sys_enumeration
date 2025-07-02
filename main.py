
'''THis is the main start program, will be the begging of the enumeration, providing a path to server or client functionality.'''

import threading

from servers.server import Server
from clients.c_base import Client

def main():
    while True:
        mode_select = input(">_ Mode selection UX, please select one of the displayed modes.\n  [1] Initiate server \n  [2] Client mode \n  [(e)xit] End process \n User input > ").strip()

        if mode_select == '1': # server
            print('server selected.. \n')

            '''Ip input with exit options (More error handling will be added once sockets are ready for testing)'''
            ip_input = input(">_ Enter IPv4 address to bind sever (default 0.0.0.0) > ") or "0.0.0.0"
            if ip_input.lower() in ['e', 'exit']:
                break
            ip = ip_input

            '''port input with exit options (More error handling will be added once sockets are ready for testing)'''
            port_input = input('>_ Enter open port to listen on. > ')
            if port_input.lower() in ['e', 'exit']:
                break
            port = int(port_input)

            server = Server(ip, port)
            threading.Thread(target=server.start).start()

        elif mode_select == '2': # client
            print('client selected... \n')

            '''Ip input with exit options (More error handling will be added once sockets are ready for testing)'''
            ip_input = input(">_ Enter server's IPv4 address > ").strip()
            if ip_input.lower() in ['e', 'exit']:
                break
            ip = ip_input

            '''port input with exit options (More error handling will be added once sockets are ready for testing)'''
            port_input = input('>_ Enter servers port. > ').strip()
            if port_input.lower() in ['e', 'exit']:
                break
            port = int(port_input)

            client = Client(ip, port)
            client.run()

        elif mode_select.lower() in ['e', 'exit']: # close program
            print('Exiting program... \n')
            break

        else: # input error handling
            print('Invalid input. Please, try again.\n')


if __name__ == "__main__":
        main()