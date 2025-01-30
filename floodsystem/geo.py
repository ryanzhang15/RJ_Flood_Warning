# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from  .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    """This function takes a list of MonitoringStation objects and a coordinate p, returning a list of (station, distance) tuples sorted by distance from p."""

    station_dist = [] # Create an empty list to store tuples of (station, distance to p)
    for station in stations:
        dist = haversine(station.coord, p, unit=Unit.KILOMETERS) # Calculate the distance between p and the station using the haversine formula
        station_dist.append((station,  dist))

    return sorted_by_key(station_dist, 1) # Return the list, sorted by distance