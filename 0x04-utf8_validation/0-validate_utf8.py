#!/usr/bin/python3
"""0-validate_utf8.py"""


def validUTF8(data):
    """validates utf-8"""
    NUMBER_OF_BITS_PER_BLOCK = 8
    MAX_NUMBER_OF_ONES = 4
    index = 0
    if len(data) > 1100:
        return False
    while index < len(data):
        number = data[index] & (2 ** 7)
        number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
        if number == 0:
            index += 1
            continue
        number_of_ones = 0
        while True:
            number = data[index] & (2 ** (7 - number_of_ones))
            number >>= (NUMBER_OF_BITS_PER_BLOCK - number_of_ones - 1)
            if number == 1:
                number_of_ones += 1
            else:
                break
            if number_of_ones > MAX_NUMBER_OF_ONES:
                return False
        if number_of_ones == 1:
            return False
        index += 1
        if index >= len(data) or index >= (index + number_of_ones - 1):
            return False
        for i in range(index, index + number_of_ones - 1):
            try:
                number = data[i]
            except:
                return False
            number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
            if number != 1:
                return False
            number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
            if number != 0:
                return False
            index += 1
    return True
