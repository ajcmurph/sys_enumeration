
 '''Server'''

import socket
import threading
import platform
import json

from commands.sys_info import get_users
from commands.proc__info import get_processes

class Server:
    def __init__(self, host = '0.0.0.0', port = 8888):
        self.host = host
        self.port = port
        self.sys = platform.system()

    def