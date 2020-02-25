import json
import os
import time
def delete(servername):
    print("Rollback server: " + servername)
    print("Roll back to: Plain/-1.0")
    print("Beginning under 3 secounds.")
    print("This program is design for both Windows/Linux, so you might seen a error, this is pretty normal.")
    time.sleep(3)
    print("Deleting...")
    print("Reading server list...")
    with open("storage/map.json", "r") as cserver:
        map = json.load(cserver)
    with open("storage/map.json", "w") as cserver:
        map.remove(servername)
        json.dump(map, cserver)
        os.system("cd storage && rmdir /s /q " + servername)
    print("Ok.")