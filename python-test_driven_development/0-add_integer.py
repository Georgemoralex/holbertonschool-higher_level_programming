#!/usr/bin/python3

"""
Documentation
Function that adds 2 integers. 
"""

def add_integer(a, b=98):
    """Returns an integer: the addition of a and b"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a == float:
        int(a)
    if b == float:
        int(b)
    
    return (a+b)