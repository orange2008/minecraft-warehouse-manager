try:
    import time
    import requests
    import time
    import json
    import newserver as ns
    import remserver as rs
    import os
    print("Minecraft Storage Management.")
    print("License: Ultimate/Forever")
    print("Server you want to join, or type 'ds' to delete some server: ")
    with open("storage/map.json") as server_choice:
        dicts = server_choice.read()
    servername = input(">> ")
    print("Resolving...")
    if servername in dicts:
        print("Connecting...")
        os.system("main.py")
    elif servername == "ds":
        print("Server you want to delete: ")
        delserver = input(">> ")
        rs.delete(delserver)
    else:
        print("Cannot establish connection to server.Creating a new server...")
        ns.create(servername)
        os.system("pause")

except KeyboardInterrupt:
    print("Roger that!")
    print("Shutting down...")
    import time
    print("Connecting to tty server...")
    print("Establishing Secure Socket Layer...")
    with open("storage/otmssl.crt") as ssl:
        crt = ssl.read()
    credit = []
    credit.append("loginas:remote")
    credit.append("username:systemctl")
    credit.append("password:" + crt)
    credit.append("run:killpce sys")
    tty = "Login Credit: " + str(credit)
    ttysays = "Process(es) systemctl@tty.local login as 10.*.*.2"
    print(ttysays)
    ttysays = "Running:'killpce sys' as user 'systemctl'. Command Permission:'root'"
    print("tty server expectedly closed.")
    print("Lost Connection to tty server.")
    print(":(")
    print("SYSTEM CRASHED: ")
    print("Please submit the crash file to https://github.com/orange2008/minecraft-warehouse-manager")
    print("ERR CODE: ERR::TTYSERV:FALSE")
    print("CAUSE: SYSTEMCTL@TTY CLOSED")
    print("SOURCE: USER@LSERV $ ^C")
    print("Creating crash file...")
    with open("./crash.log", 'w') as crashlog:
        crashlog.write("Errcode: ERR::TTYSERV:FALSE\n")
        crashlog.write("Cause: systemctl@tty closed system service\n")
        crashlog.write("Source: user@localservice $BOOT $ ^C\n")
        crashlog.write("Internal Err: KeyboardInterrupt\n")
        crashlog.write("Data lost: 0.00%, 0 byte data lost.\n")
        crashlog.write("Create program: /program/system.app\n")
        crashlog.write("Severity: Nothing serious.\n")
        crashlog.write("Need data recovery: False\n")
    print("Quitting...")