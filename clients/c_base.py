'''THis handles the base client side functionality of connecting to the server's socket and sending the clients input to the server machine'''

import socket
import json

class Client:
    def __init__(self, ip: str, port: int, commands: list):
        self.ip = ip
        self.port = port
        self.commands = commands

    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((self.ip, self.port))
                print(f">_ Connected to {self.ip}:{self.port} <\n")

                for cmd in self.commands:
                    print(f">_ Sending command: {cmd} <\n")
                    s.sendall(cmd.encode())
                    response = s.recv(4096)

                    try:
                        result = json.loads(response.decode())
                        print(f">_ [{self.ip}] Response: {result} <\n")
                    except json.JSONDecodeError:
                        print(f"[{self.ip}] Invalid JSON response: {response.decode()}")

        except Exception as e:
            print(f">_ [!] Connection failed to {self.ip}:{self.port} — {e} [!] <")
