import time
import os

seconds = int(input("Seconds to countdown: "))

for i in range(seconds, -1, -1):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Time left: {i}s")
    time.sleep(1)

print("Time is up!")