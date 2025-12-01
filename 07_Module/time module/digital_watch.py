import time as t
import os

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(t.strftime("%I:%M:%S"))
    t.sleep(1)