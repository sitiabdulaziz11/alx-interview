#!/usr/bin/python3
"""
UTF-8 Validation
"""


def is_continuation(byte, indx, no_bytes):
    """
    Check if a byte is a continuation byte
    """
    i = 0
    while i < no_bytes and indx < len(byte):
        if not ((byte[indx] & (0b10000000)) != 0 and (
                                                byte[indx] & (1 << 6)) == 0):
            return False
        i += 1
        indx += 1
    if i != no_bytes:
        return False
    return True


def validUTF8(data):
    """
    A function that validates whether a list of
    integers represents a valid UTF-8 encoding.
    It checks the bytes in the list against UTF-8
    encoding rules and returns True if the list is valid,
    otherwise, it returns False.
    """
    i = 0
    while i < len(data):
        byte = data[i]
        bit = 7
        if (byte & 0b10000000) == 0:
            i += 1
        elif (byte & (1 << bit)) != 0:
            bit -= 1
            if (byte & (1 << bit)) != 0:
                bit -= 1
                if (byte & (1 << bit)) == 0:
                    i += 1
                    result = is_continuation(data, i, 1)
                    i += 1
                    if not result:
                        return False
                elif (byte & (1 << bit)) != 0:
                    bit -= 1
                    if (byte & (1 << bit)) == 0:
                        i += 1
                        result = is_continuation(data, i, 2)
                        i += 2
                        if not result:
                            return False
                    elif (byte & (1 << bit)) != 0:
                        bit -= 1
                        if (byte & (1 << bit)) == 0:
                            i += 1
                            result = is_continuation(data, i, 3)
                            i += 3
                            if not result:
                                return False
                        else:
                            return False
    return True
