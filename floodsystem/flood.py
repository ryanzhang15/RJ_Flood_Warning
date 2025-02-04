# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT

from .utils import sorted_by_key  # noqa

"""This module contains a collection of functions related to flood data.

"""


def stations_level_over_threshold(stations, tol):
    """This function takes a list of MonitoringStation objects and a float tol, returning a list of tuples (MonitoringStation, float) of stations with a latest relative water level over tol."""

    stations_level = [] # Create a list to return    
    for i in stations:
        if i.relative_water_level() is not None and i.relative_water_level() > tol: 
            stations_level.append((i, i.relative_water_level()))

    return sorted_by_key(stations_level, 1, reverse=True) # Return the list, sorted by relative water level in descending order