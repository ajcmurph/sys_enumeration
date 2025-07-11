
'''THe more impresive thing in this program client_ui handles the clients user input and enables multi-threading, to queue multiple commands for multiple servers'''

import threading
from clients.c_base import Client

def start_client(ip, port, commands):
    client = Client(ip, port, commands)
    client.run()

def client_mode():
    targets = []

    print("\n>_ Multi-host Client Mode <")
    print(">_ Enter multiple server targets. Type '(f)inish' to continue. <\n")

    while True:
        # multiple exit options, no real point just for user ease of use
        ip = input("Server IP ('(f)inish'): ").strip()
        if ip.lower() in ('f', 'finish', 'e', 'exit'):
            break

        port_input = input(">_ Port: ").strip()
        if port_input.lower() in ('e', 'exit'):
            break

        try:
            port = int(port_input)
        except ValueError:
            print(">_ [!] Invalid port. Please enter a number. [!] <\n")
            continue

        # displays the user options, and a list for the commands from the cmd input to be appended to for use in threads
        commands = []
        print(
            ">_ Command selection. Please select on of predefined commands:\n"
            "  [1] get_users \n"
            "  [2] get_processes \n"
            "  [(e)xit] end process \n"
            "  [(f)inish] to continue \n"  
            "\nUser input: "
        )

        while True:

            cmd = input("Command: ").strip()
            # multiple exit options, no real point just for user ease of use
            if cmd.lower() in ('f', 'finish', 'e', 'exit'):
                break

            # error handling, makes sure its a valid command (1 or 2 - at this point)
            if cmd not in ('1', '2'):
                print(">_ [!] Invalid command. [!] <")
                continue


            commands.append(cmd)

        if commands:
            targets.append((ip, port, commands))

        # Handles the multi-threading. Threads is a list of the inputed ips and commands that follow the order in they were entered to create first in first out queue. to handle multiple server connections and commands.
    threads = []
    for ip, port, commands in targets:
        t = threading.Thread(target=start_client, args=(ip, port, commands))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
