
 '''Server'''

import socket
import threading
import platform
import json

from commands.sys_info import get_users
from commands.proc__info import get_processes

class Server:
    def __init__(self, host = '0.0.0.0', port = 8888):
        self.host_ip = host
        self.port = port
        self.sys = platform.system()

    '''Socket connection using AF_INET whihc uses the server hosts IPv4 address and a port to set up a connection'''
    def start(self):
        print(f">_ Server initiated... ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:


            try:
                s.settimeout(45) # 45 seconds timer for the connection to be made...
                s.bind((self.host_ip, self.port)) # Blind the ip and port to soc for AF_INET
                s.listen(5) # Listen for connection

                print(f">_ Listening for a connection... \n  {self.sys} host -  {self.host_ip}:{self.port} <")

                while True:
                    conn, addr = s.accept()
                    threading.Thread(target=self.client_handler, args=(conn, addr))


            except socket.timeout:
                print('Host session timed out. No connection was made within 45 seconds.')
            finally:
                s.close()




    def client_handler(self, conn, addr):
        print(f">_ Connected to {addr} <")
        with conn:
            try:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    command = data.decode().strip()
                    print(f">_ {addr} | Command recieved: {command} <")
                    send = self.exe_command(command)
                    conn.sendall(json.dumps(send).encode())

            except Exception as e:
                    print(f">_ [!] Error with {addr}: {e} <")
                    conn.sendall(b'{"error": "Server eorror"}')


    def exe_command(self, command):
        if command == '1':
            return get_users()

        elif command == '2':
            return get_processes()

        #elif command in ['e', 'exit']:

        else:
            return {'error': 'invalid command'}