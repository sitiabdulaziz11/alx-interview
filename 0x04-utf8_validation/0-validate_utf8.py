#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    if not data:
        return True

    i = 0
    while i < len(data):
        byte = data[i]

        # Single-byte character (ASCII)
        if byte < 128:
            i += 1
            continue

        # Determine the number of bytes for multi-byte characters
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

        # Check continuation bytes
        i += 1
        for _ in range(num_bytes - 1):
            if i >= len(data) or not is_continuation(data[i]):
                return False
            i += 1

    return True
