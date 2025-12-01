import time
import sys

for i in range(101):
    # Progress ....
    bar = "█" * (i // 5) + "-" * (20 - (i // 5))
    # \r cursor stay on same line
    sys.stdout.write(f"\rLoading: [{bar}] {i}%")
    sys.stdout.flush()
    time.sleep(0.05)

print("Completed!")
