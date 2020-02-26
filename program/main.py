def mainapp(servername):
    import json
    import pygal
    import matplotlib
    import requests
    import datetime
    import os
    import time
    import store
    import takeout
    import delit
    import see
    import seenaq
    print("Establishing secure connection...")
    with open("storage/otmssl.crt", "a") as certificate:
        date = datetime.date.today()
        certificate.write("\n")
        certificate.write(str(date))
    print("Established.")
    print("Connected.")
    print("What do you want to do?")
    print("1. Store things in the warehouse.")
    print("2. Take things out of the warehouse.")
    print("3. Delete the specified item in the warehouse.")
    print("4. See everything in the warehouse.")
    print("5. View the name and quantity of everything in the warehouse.")
    while True:
        sth = input(">> ")
        if sth == "1":
            store.store(servername)
        elif sth == "2":
            takeout.takeout(servername)