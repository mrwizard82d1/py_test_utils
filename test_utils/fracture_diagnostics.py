import random

from faker import Faker

import test_utils.core as tuc

import cytoolz.curried as cytoolz

fake = Faker(['la'])

LENGTH_UNITS = ['m', 'ft']
M_PER_FT = 0.3048


class Measurement:
    """Class modeling a physical measurement."""
    magnitude: float
    unit: str

    def __init__(self, magnitude, unit):
        """
        Construct a measurement of `magnitude` measured in `unit`.

        Args:
            magnitude: The magnitude of the measurement.
            unit: The unit of the measurement.

        Returns:
            The constructed measurement.
        """
        self.magnitude = magnitude
        self.unit = unit

    def __repr__(self):
        """
        Returns:
            The human-readable representation of this instance
        """
        return f"{self.magnitude} {self.unit}"


def ft_to_m(length_ft):
    """
    Convert a length in ft to m.

    Args:
        length_ft: A length in feet.

    Returns:
        The same length measured in meters.
    """
    return M_PER_FT * length_ft


def fracture_length(unit=None):
    """
    Return a random fracture length in `unit` (m or ft) units. If units are *not* specified,
    select a random length unit.

    Args:
        unit: The length unit of the returned measurement.

    Returns:
       A random fracture length in `unit` units.
    """
    fracture_length_in_feet = tuc.draw_normal(773, 106)

    if unit is None:
        unit = random.choice(LENGTH_UNITS)

    if unit == 'ft':
        return Measurement(fracture_length_in_feet, 'ft')
    elif unit == 'm':
        return Measurement(fracture_length_in_feet * M_PER_FT, 'm')
    else:
        raise ValueError(f'Unrecognized length unit: "{unit}"')


def fracture_height(unit=None):
    """
    Return a random fracture height in `unit` (m or ft) units.

    Args:
        unit: The height unit of the returned measurement.

    Returns:
       A random fracture height in `unit` units.
    """
    fracture_height_in_feet = tuc.draw_normal(248.6, 63.)

    if unit is None:
        unit = random.choice(LENGTH_UNITS)

    if unit == 'ft':
        return Measurement(fracture_height_in_feet, 'ft')
    elif unit == 'm':
        return Measurement(fracture_height_in_feet * M_PER_FT, 'm')
    else:
        raise ValueError(f'Unrecognized height unit: "{unit}"')

