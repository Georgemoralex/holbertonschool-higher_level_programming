#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a == float:
        int(a)
    if b == float:
        int(b)
    
    return (a+b)