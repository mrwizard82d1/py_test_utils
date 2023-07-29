import datetime
import random

from faker import Faker

import cytoolz.curried as cytoolz


fake = Faker()


def rand_digit() -> int:
    """
    Generates a single, randomly distributed digit [0-9].

    Returns:
        The generated digit.
    """
    return fake.random_number(digits=1)


def rand_2() -> int:
    """
    Generates a single, randomly generated 2-digit number.

    Returns:
        The generated 2-digit number.
    """
    return fake.random_number(digits=2)


def rand_3() -> int:
    """
    Generates a single, randomly generated 3-digit number.

    Returns:
        The generated 3-digit number.
    """
    return fake.random_number(digits=3)


def rand_4() -> int:
    """
    Generates a single, randomly generated 4-digit number.

    Returns:
        The generated 4-digit number.
    """
    return fake.random_number(digits=4)


def rand_5() -> int:
    """
    Generates a single, randomly generated 5-digit number.

    Returns:
        The generated 5-digit number.
    """
    return fake.random_number(digits=5)


def rand_6() -> int:
    """
    Generates a single, randomly generated 6-digit number.

    Returns:
        The generated 6-digit number.
    """
    return fake.random_number(digits=6)


def rand_7() -> int:
    """
    Generates a single, randomly generated 7-digit number.

    Returns:
        The generated 7-digit number.
    """
    return fake.random_number(digits=7)


def rand_8() -> int:
    """
    Generates a single, randomly generated 8-digit number.

    Returns:
        The generated 8-digit number.
    """
    return fake.random_number(digits=8)


def rand_9() -> int:
    """
    Generates a single, randomly generated 9-digit number.

    Returns:
        The generated 9-digit number.
    """
    return fake.random_number(digits=9)


def rand_alpha() -> str:
    """
    Generates a single, randomly generated (ASCII) letter.

    Returns:
        The generated letter.
    """
    return fake.random_letter()


def rand_alphas(count: int = 16) -> str:
    """
    Generate a list of size `count` random, ASCII letters.
    Args:
        count: The number of characters in the sequence.

    Returns:
        A random sequence of count single character strings.
    """
    return fake.random_letters(count)


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

    return cytoolz.map(lambda _: distribution_func(), range(count))
