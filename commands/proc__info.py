'''THis application hanles the command for getting the running proccesses for windows and linux devices'''

import platform
import subprocess
import os

def get_processes():
    sys_type = platform.system()
    proc = []

    try:
            # Linux - Reads the /proc file to see running processes
        if sys_type == "Linux":
            for pid in os.listdir('/proc'):
                if pid.isdigit():
                    try:
                        with open(f'/proc/{pid}/comm') as f:
                            name = f.read().strip()
                            # Formating command output
                        proc.append({"Name": name, "PID": pid})

                        if len(proc) >= 15:
                            break
                    except:
                        continue

            # Windows - uses subprocess to enter commands to read tasklist in cmd
        elif sys_type == "Windows":
            shell_outp = subprocess.check_output('tasklist', shell=True).decode()
            lines = shell_outp.splitlines()[3:]

            for line in lines[:15]:
                sections = line.split()
                if len(sections) >= 2:
                     # Formating command output
                    proc.append({"Name": sections[0], "PID": sections[1]})

        return {"Processes": proc}

    except Exception as e:
        return {"error": str(e)}
