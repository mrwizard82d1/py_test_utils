import random

from faker import Faker

import test_utils.core as tuc

import cytoolz.curried as cytoolz

fake = Faker(['la'])

LENGTH_UNITS = ['m', 'ft']
M_PER_FT = 0.3048

FRACTURE_AZIMUTH_TYPES = ['project', 'manual', 'ms_stage']


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

    def __neg__(self):
        """
        Returns:
            The same measurement with a negative magnitude.
        """
        return Measurement(-self.magnitude, self.unit)

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


def length_measurement(magnitude_in_feet_func, unit=None):
    """
    Return a random length measurement in `unit` (m or ft) units. If units are *not* specified,
    select a random length unit.

    Args:
        magnitude_in_feet_func: A function taking no arguments and returning an appropriate length in feet.
        unit: The length unit of the generated measurement.

    Returns:
       A random length measurement in `unit` units.
    """
    length_in_feet = magnitude_in_feet_func()

    if unit is None:
        unit = random.choice(LENGTH_UNITS)

    if unit == 'ft':
        return Measurement(length_in_feet, 'ft')
    elif unit == 'm':
        return Measurement(length_in_feet * M_PER_FT, 'm')
    else:
        raise ValueError(f'Unrecognized length unit: "{unit}"')


def fracture_length(unit=None):
    """
    Return a random fracture length in `unit` (m or ft) units. If units are *not* specified,
    select a random length unit.

    Args:
        unit: The length unit of the returned measurement.

    Returns:
       A random fracture length in `unit` units.
    """
    return length_measurement(lambda: tuc.draw_normal(773, 106), unit)


def fracture_height(unit=None):
    """
    Return a random fracture height in `unit` (m or ft) units.

    Args:
        unit: The height unit of the returned measurement.

    Returns:
       A random fracture height in `unit` units.
    """
    return length_measurement(lambda: tuc.draw_normal(248.6, 63.), unit)


def lateral_shift_positive_east(unit=None):
    """
    Return a random lateral shift `unit` (m or ft) units. If units are *not* specified, select a random length unit.
    Positive values indicate an eastward shift relative to well bore north; negative values indicate a westward shift
    relative to well bore north.

    Args:
        unit: The optional length unit of the returned shift.

    Returns:
       A random lateral shift in `unit` units.
    """
    directionless_lateral_shift = length_measurement(lambda: 20 * random.random(), unit)

    is_eastward = random.choice([True, False])
    return directionless_lateral_shift if is_eastward else -directionless_lateral_shift


def vertical_shift_positive_down(unit=None):
    """
    Return a random vertical shift `unit` (m or ft) units. If units are *not* specified, select a random length unit.
    Positive values indicate a downward shift relative to ground level; negative values indicate an upward shift
    relative to ground level.

    Args:
        unit: The optional length unit of the returned shift.

    Returns:
       A random vertical shift in `unit` units.
    """
    directionless_vertical_shift = length_measurement(lambda: 50 * random.random(), unit)

    is_downward = True if random.randrange(100) < 85 else False
    return directionless_vertical_shift if is_downward else -directionless_vertical_shift


def random_fracture_azimuth_type():
    """
    Returns:
        A random fracture azimuth type ('project', 'manual', or 'ms-stage').
    """
    return random.choice(FRACTURE_AZIMUTH_TYPES)


def manual_fracture_azimuth_east_of_north():
    """
    Calculate a random manual fracture azimuth relative to east of north.

    Returns:
        The calculated manual fracture azimuth.
    """
    return Measurement(random.randrange(0, 360), 'deg')
