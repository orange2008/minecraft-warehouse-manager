import json
import pygal
import matplotlib
import requests
import datetime
import os
import time
print("Establishing secure connection...")
with open("storage/otmssl.crt", "a") as certificate:
    date = datetime.date.today()
    certificate.write("\n")
    certificate.write(str(date))
print("Established.")
print("Connected.")