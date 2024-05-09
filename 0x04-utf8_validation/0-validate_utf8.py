#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Method that determines if a given
    data set represents a valid UTF-8 encoding.
    """
    def is_continuation(byte):
        """
        Helper function to check if a byte is a continuation byte
        """
        return byte & 0b11000000 == 0b10000000

    if not data:
        return False
    for byte in data:
        if byte < 128:
            continue
        if byte < 192:
            return False
        elif byte < 224:
            num_bytes = 2
        elif byte < 240:
            num_bytes = 3
        elif byte < 248:
            num_bytes = 4
        else:
            return False

        for _ in range(num_bytes - 1):
            byte = data.pop(0)
            if byte is None or not is_continuation(byte):
                return False
    return True
