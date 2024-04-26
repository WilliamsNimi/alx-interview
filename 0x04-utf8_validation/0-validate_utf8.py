#!/usr/bin/env python3
"""utf8 validation module"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ checks to see if dataset is valid UTF8
    @data: data set to be validates
    Return: True or False
    """
    pos = 0
    for byte in data:
        if pos == 0:
            if byte >> 7 == 0b0:
                pos = 0
            elif byte >> 5 == 0b110:
                pos = 1
            elif byte >> 4 == 0b1110:
                pos = 2
            elif byte >> 3 == 0b11110:
                pos = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            pos -= 1
    return pos == 0
