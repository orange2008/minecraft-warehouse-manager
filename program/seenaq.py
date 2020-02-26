def seenaq(servername):
    import json
    print("Outputting...")
    server = "storage/" + servername + "/item.json"
    with open(server) as seeall:
        everything = json.load(seeall)
    for name, quantity in everything.items():
        print("You have " + quantity + " " + name)