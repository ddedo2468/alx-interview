#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    num_of_bytes = 0
    for char in data:
        bin = format(char, "#010b")[-8:]
        if num_of_bytes == 0:
            if bin.startswith("0"):
                continue
            elif bin.startswith("110"):
                num_of_bytes = 1
            elif bin.startswith("1110"):
                num_of_bytes = 2
            elif bin.startswith("11110"):
                num_of_bytes = 3
            else:
                return False
        else:
            if not bin.startswith("10"):
                return False
            num_of_bytes -= 1
    return num_of_bytes == 0
