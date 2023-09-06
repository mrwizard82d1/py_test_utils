from faker import Faker

import cytoolz.curried as cytoolz

lorem_fake = Faker(['la'])


def rand_words(count=5):
    """
    Generate `count` words from "lorem ipsum" (Latin) text.

    Args:
        count: The number of random words to generate.

    Returns:
        A list containing `count` random Latin words.
    """
    return lorem_fake.words(count)


def rand_word():
    """
    Generate a single random word from "lorem ipsum" (Latin) text.

    Returns:
        A single random Latin words.
    """
    return rand_words(count=1)
