def takeout(servername):
    import json
    import sys
    import os
    item = 0
    itemname = input("Please enter the item name: ")
    itemquantity = input("Please enter the number of items to be taken out: ")
    print("Storing...")
    server = "storage/" + servername + "/item.json"
    with open(server, 'r') as reading:
        localdict = json.load(reading)
    with open(server, 'r') as reading:
        backupdict = reading.read()
    with open(server, 'w') as storing:
        try:
            item = localdict[itemname]
        except KeyError:
            print("This item never stored.")
            localdict[itemname] = 0
            pass
        finally:
            try:
                item = int(item) - int(itemquantity)
            except ValueError:
                print("The number of items you entered is not a number.")
                print("For database security, we urgently shut down files and servers. An error report is being generated. . .")
                with open("./crash.log", 'w') as crashlog:
                    crashlog.write("Errcode: ERR::FAILED:TO:CONVERT:STRING:TO:INT\n")
                    crashlog.write("Cause: Cannot convert string to int because user entered a string, not a number.\n")
                    crashlog.write("Source: user@localservice store.app $ int = string then error\n")
                    crashlog.write("Internal Err: ValueError: invalid liitelal for int() with base 10: $string\n")
                    crashlog.write("Data lost: 0.00%, 0 byte data lost.\n")
                    crashlog.write("Create program: /program/store.app\n")
                    crashlog.write("Severity: CRITICAL.\n")
                    crashlog.write("Need data recovery: Can be restored by built-in data recovery software.\n")
                    print(":(")
                    print("CRITICAL ERROR!")
                    print("SYSTEM CRASHED!")
                    print("POWERING OFF...")
                    print("RECOVERING DATA...")
                    with open(server, 'w') as recover:
                        recover.write(backupdict)
                    print("TERMINATING PROCESS...")
                    print('SUCCESS: The process "python.exe" with PID 6660 has been terminated.')
                    os._exit(0)
            except KeyError:
                print("This item never stored.")
                localdict[itemname] = 0
                pass
        localdict[itemname] = item
        json.dump(localdict, storing)
    print("Ok.")