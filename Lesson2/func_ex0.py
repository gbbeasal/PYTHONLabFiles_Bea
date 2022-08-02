__all__ = (
    'empty_func', 'add_numbers', 'get_location',
)

import os
import random

VERBOSE = True


def empty_func():
    """This function does not do anything

    NOTE: All functions return a value. Default value is None

    """


def add_numbers(n1, n2):
    """This function returns a tuple

    NOTE: This function accepts 2 positional arguments

    """
    out = n1 + 1, n2 + 1, n1 + n2
    if VERBOSE:
        print(out)
    return out


def get_location(loc, zipcode=123, city=None):
    """

    This function accepts a keyword argument with a
    default value.

    """
    city = city or 'No city'
    out = f'{loc}, {zipcode}: {city}'
    if VERBOSE:
        print(out)
    return out







