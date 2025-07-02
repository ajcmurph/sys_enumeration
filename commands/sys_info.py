
'''Command functions dependent on operating system, to make the enumeration work on both windows and linux'''

import platform
import subprocess

def get_users():
    sys_type = platform.system() # get sys name

    try:

        '''Linux is the easiest to enumerate as the file system is more accessable'''

        if sys_type == "Linux": # checks if the operating system is Linux-based
            with open('/etc/passwd') as f: # reads the passwd file to get sys users
                sys_users = [line.split(':')[0] for line in f] # formating the /etc/passwd file
            return {"System users :": sys_users}



        '''Windows enumeration takes more, as windows isnt as open with its directory architecture as Linux, though with use of shell commands it should be fine'''

        elif sys_type == "Windows": # checks if the operating system is windows

            shell_outp = subprocess.check_output('net user', shell = True).decode()

            sys_users = [] # unformated users sent to list
            collect = False

            for line in shell_outp.splitlines():
                if "----" in line:
                    collect = not collect
                    continue
                if collect:
                    sys_users += line.split()

        return {"System users :": sys_users}




    except Exception as e:
        return {"error": str(e)}