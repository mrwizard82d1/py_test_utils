#
# This file is part of Orchid and related technologies.
#
# Copyright (c) 2017-2020 Reveal Energy Services.  All Rights Reserved.
#
# LEGAL NOTICE:
# Orchid contains trade secrets and otherwise confidential information
# owned by Reveal Energy Services. Access to and use of this information is 
# strictly limited and controlled by the Company. This file may not be copied,
# distributed, or otherwise disclosed outside of the Company's facilities 
# except under appropriate precautions to maintain the confidentiality hereof, 
# and may not be used in any way not expressly authorized by the Company.
#

import datetime
import random
import string

import toolz


def rand_digit() -> int:
    """
    Generates a single, randomly distributed digit [0-9].

    Returns:
        The generated digit.
    """
    return random.randrange(10)


def rand_2() -> int:
    """
    Generates a single, randomly generated 2-digit number.

    Returns:
        The generated 2-digit number.
    """
    return random.randrange(100)


def rand_3() -> int:
    """
    Generates a single, randomly generated 3-digit number.

    Returns:
        The generated 3-digit number.
    """
    return random.randrange(1000)


def rand_4() -> int:
    """
    Generates a single, randomly generated 4-digit number.

    Returns:
        The generated 4-digit number.
    """
    return random.randrange(10000)


def rand_5() -> int:
    """
    Generates a single, randomly generated 5-digit number.

    Returns:
        The generated 5-digit number.
    """
    return random.randrange(100000)


def rand_6() -> int:
    """
    Generates a single, randomly generated 6-digit number.

    Returns:
        The generated 6-digit number.
    """
    return random.randrange(1000000)


def rand_7() -> int:
    """
    Generates a single, randomly generated 7-digit number.

    Returns:
        The generated 7-digit number.
    """
    return random.randrange(10000000)


def rand_8() -> int:
    """
    Generates a single, randomly generated 8-digit number.

    Returns:
        The generated 8-digit number.
    """
    return random.randrange(100000000)


def rand_9() -> int:
    """
    Generates a single, randomly generated 9-digit number.

    Returns:
        The generated 9-digit number.
    """
    return random.randrange(1000000000)


def rand_alpha() -> str:
    """
    Generates a single, randomly generated (ASCII) letter.

    Returns:
        The generated letter.
    """
    return random.choice(string.ascii_letters)


def rand_alphas(count: int = -1) -> str:
    """
    Generate a possibly infinite sequence of randomly generated (ASCII) letters.
    Args:
        count: The number of characters in the sequence (-1 indicates infinite).

    Returns:
        The random sequence of single character strings of the specified length.
    """
    def infinite_alphas() -> str:
        while True:
            yield random.choice(string.ascii_letters)

    if count > 0:
        return toolz.take(count, infinite_alphas())
    else:
        return infinite_alphas()


def rand_time_stamp(begin_year: int, end_year: int) -> datetime.datetime:
    """
    Generate a random time stamp for years `begin_year` to (and including) `end_year`.

    Args:
        begin_year: The minimum year of the generated time stamps.
        end_year: The maximum year of the generated time stamps.

    Returns:
        The generated time stamp.

    """
    while True:
        try:
            return datetime.datetime(random.randrange(begin_year, end_year + 1), random.randrange(1, 12 + 1),
                                     random.randrange(1, 31 + 1), random.randrange(24), random.randrange(60),
                                     random.randrange(60))
        except ValueError:
            # Try again. Will eventually generate a valid value.
            pass


def draw_normal(mu: float = 0, sigma: float = 1.0) -> float:
    """
    Generate a single random value normally distributed with mean, `mu`, and standard deviation, `sigma`.

    Args:
        mu: The mean of the normal distribution (default = 0.0).
        sigma: The standard deviation of the normal distribution (default = 1.0).

    Returns:
        The value "drawn" from the specified distribution.
    """
    return random.gauss(mu, sigma)


def sample_normal(mu: float = 0, sigma: float = 1.0, count: int = 3) -> float:
    """
    Generate `count` random values normally distributed with mean, `mu`, and standard deviation, `sigma`.

    Args:
        mu: The mean of the normal distribution (default = 0.0).
        sigma: The standard deviation of the normal distribution (default = 1.0).
        count: The number of samples to return (default=3).

    Returns:
        The sequence of `count` values "drawn" from the specified distribution.
    """
    def distribution_func():
        return draw_normal(mu, sigma)

    return toolz.map(lambda _: distribution_func(), range(count))
