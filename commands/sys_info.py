'''THis application handles the command for getting the system users for windows and linux devices'''

import platform
import subprocess

def get_users():
    sys_type = platform.system() # checks machines operating system

    try:
            # LInux - reads the first line of the /etc/passwd and prints it
        if sys_type == "Linux":
            with open('/etc/passwd') as f:
                 # formating
                sys_users = [line.split(':')[0] for line in f]
            return {"System users": sys_users}


            # Windows - uses subprocesses to input a command such as net user to get the systems users
        elif sys_type == "Windows":
            shell_outp = subprocess.check_output('net user', shell=True).decode()
            sys_users = []
            collect = False
                # formating
            for line in shell_outp.splitlines():
                if "----" in line:
                    collect = not collect
                    continue
                if collect:
                    sys_users += line.split()

            return {"System users": sys_users}

        else:
            return {"error": "Unsupported OS"}

    except Exception as e:
        return {"error": str(e)}