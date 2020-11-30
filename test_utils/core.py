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

import random
import string

import toolz


def rand_digit():
    return random.randrange(10)


def rand_2():
    return random.randrange(100)


def rand_3():
    return random.randrange(1000)


def rand_4():
    return random.randrange(10000)


def rand_5():
    return random.randrange(100000)


def rand_6():
    return random.randrange(1000000)


def rand_7():
    return random.randrange(10000000)


def rand_8():
    return random.randrange(100000000)


def rand_9():
    return random.randrange(1000000000)


def rand_alpha():
    return random.choice(string.ascii_letters)


def rand_alphas(n=0):
    def infinite_alphas():
        while True:
            yield random.choice(string.ascii_letters)

    if n > 0:
        return toolz.take(n, infinite_alphas())
    else:
        return infinite_alphas()
