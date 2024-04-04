#!/usr/bin/python3
""" represents a valid UTF-8 encoding. """

def get_leading_ones(byte):
    """ returns the number of leading ones in a byte """
    mask = 1 << 7
    leading_ones = 0
    while byte & mask:
        leading_ones += 1
        mask = mask >> 1
    return leading_ones


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    num_bytes = 0
    for byte in data:
        if num_bytes:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1
            continue
        num_bytes = get_leading_ones(byte)
        if num_bytes == 1 or num_bytes > 4:
            return False
        num_bytes = max(num_bytes - 1, 0)
    return num_bytes == 0
