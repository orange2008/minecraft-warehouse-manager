import json
import os
def create(servername):
    print("Checkout: ")
    print("Server name: " + servername)
    print("Creating server...")
    os.system('cd storage && mkdir ' + servername + ' && cd ' + servername + ' echo "{}" >> item.json')
    print("Reading server list...")
    with open("storage/map.json", "r") as cserver:
        map = json.load(cserver)
    print("Creating server...")
    with open("storage/map.json", "w") as cserver:
        map.append(servername)
        json.dump(map, cserver)
    print("Ok.")