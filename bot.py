import time
import os

print("БОТ ЗАПУСТИЛСЯ")
print("TOKEN есть:", bool(os.getenv("TOKEN")))

while True:
    time.sleep(60)
