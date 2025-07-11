This is a simple enumeration tool for testing my local network connections. Nothing impressive, but shows general pyhton, socket, threading and software development practices.

sys_enumeration is simple and crude, entirely text-based UX it takes multiple IP's and Port's to execute predefined enumeration commands on the server machines. 

As previously stated I developed this for testing purposes to ensure communication between my vLan machines (a glorifed ping), I am well aware of its issues and intend on making a different better application using what I've learnt from the development of this application.

THIS PROGRAM IS COMPATABLE WITH WINDOWS AND LINUX SYSTEMS - although windows defender will prevent connections, so the firewall will have to be dissabled and the machines network type should be private - this info is easy to check in powershell with get-netconnectionprofile to check network category or get-netfirewallprofile and ensure private is false.

Download instruction:
	1) very simple download. Use git clone https://github.com/ajcmurph/sys_enumaration.
	2) repeat step 1 on all machines.

To start:
	1) run main.py this is the entrance program
	2) run the clinet service from one of the machines on the netwrok, then select initiate server on the rest.
	3) Input each machines ip and port on the client machine, and select any of the pre-programmed commands.
	4) When done inputing the machines ip and ports, enter (e)xit or (f)inish, all the machines should return their processes, users or both. 
