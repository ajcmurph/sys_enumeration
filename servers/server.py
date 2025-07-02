
'''Server implementation'''

import socket
import threading
import platform
import json

from commands.sys_info import get_users
from commands.proc__info import get_processes

class Server:
    def __init__(self, host='0.0.0.0', port=8888):
        self.host_ip = host
        self.port = port
        self.sys = platform.system()

    def start(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"\n>_ Server initiated at {self.host_ip}:{self.port}... <")
            try:
                s.settimeout(45)
                s.bind((self.host_ip, self.port))
                s.listen(5)

                print(f">_ Host, {self.sys} - Listening for connections... \n")

                while True:
                    conn, addr = s.accept()
                    print(f">_ Accepted connection from {addr} <")
                    threading.Thread(target=self.client_handler, args=(conn, addr)).start()  # FIXED: added .start()

            except socket.timeout:
                print('\n>_ [!] Session timed out. No connection made. [!] <')
            except Exception as e:
                print(f">_ [!] Server error: {e} [!] <")
            finally:
                s.close()

    def client_handler(self, conn, addr):
        print(f">_ Connected to {addr} <<")
        with conn:
            try:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    command = data.decode().strip()
                    print(f">_ {addr} | Command received: {command} <<")
                    response = self.exe_command(command)
                    conn.sendall(json.dumps(response).encode())

            except Exception as e:
                print(f">_ [!] Error with {addr}: {e} <")
                conn.sendall(b'{"error": "Server error"}')

    def exe_command(self, command):
        if command == '1':
            return get_users()
        elif command == '2':
            return get_processes()
        else:
            return {'error': 'Invalid command'}