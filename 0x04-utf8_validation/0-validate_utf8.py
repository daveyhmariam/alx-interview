#!/usr/bin/python3
"""
UTF-8 encoding check
"""


def validUTF8(data):
    """
    Checkes if dataset is utf-8 encoded

    Args:
        data (list): data set of integers

    Return:
        True or False
    """
    bytes = 0
    for byte in data:
        byte = byte & 0xFF
        if bytes == 0:
            if byte >> 5 == 0b110:
                bytes = 1
            elif byte >> 4 == 0b1110:
                bytes = 2
            elif byte >> 3 == 0b11110:
                bytes = 3
            elif byte >> 7 != 0:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes -= 1
    return bytes == 0
