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