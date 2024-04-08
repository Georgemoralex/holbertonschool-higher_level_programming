#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    elements = len(argv) - 1

    print(elements, end=" ")

    if elements == 1:
        print("argument", end="")
    else:
        print("arguments", end="")

    if elements == 0:
        print(".")
    else:
        print(":")

    for i in range(1, elementsac + 1):
        print("{:d}: {}".format(i, argv[i]))
