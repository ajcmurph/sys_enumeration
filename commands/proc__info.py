
 '''get_process'''

import platform
import subprocess
import os

def get_processes()
    sys_type = platform.system()
    proc = []

    '''Linux processes can be found in the usrers /proc directory, makes it easyto see the active processes'''

    try:
        if sys_type == "Linux":
            for pid in os.listdir('/proc'):
                if pid.isdigit():
                    try:
                        with open(f'/proc/{pid}/comm') as f:
                            name = f.read().strip()
                        proc.append({"pid": pid, "name:" name})

                        if len(proc) >+ 15:
                            break
                    except:
                        continue


        elif sys_type == "Windows":

            shell_outp = subprocess.check_output('tasklist', shell = True).decode()
            lines = shell_outp.splitlines()[3:]

            for line in lines[:15]:
                sections = line.split()
                if len(sections) >= 2:
                    proc.append({"pid": sections[1], "name": sections[0]})

        return {"Processes": proc}

    except Exception as e:
        return {"error": str(e)}