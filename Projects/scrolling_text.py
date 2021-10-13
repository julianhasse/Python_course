import time
import sys
s = "Julian Hasse - Welcome to the scrolling text 1234567890"
while 1:
    for i in range(80):
        print(s[i:i+80]+'\r'),
        sys.stdout.flush()
        time.sleep(0.1)
