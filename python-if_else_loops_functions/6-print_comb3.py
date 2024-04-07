#!/usr/bin/python3
for numten in range(0, 10):
    for numone in range(0, 10):
        if numone > numten and (numone + numten) < 17:
            print("{:d}{:d}".format(numten, numone), end=", ")
print("89")
