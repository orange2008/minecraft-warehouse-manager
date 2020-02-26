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
    print("3. See everything in the warehouse.")
    print("q. Exit.")
    while True:
        sth = input(">> ")
        if sth == "1":
            store.store(servername)
        elif sth == "2":
            takeout.takeout(servername)
        elif sth == "3":
            seenaq.seenaq(servername)
        elif sth == "q":
            exit()