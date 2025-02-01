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


def stations_within_radius(stations, centre, r):
    """This function takes a list of MonitoringStation objects, a coordinate for the centre, and a radius r, returning a list of stations within distance r from centre."""

    station_dist = stations_by_distance(stations, centre) # Get a list of (station, distance to center) tuples sorted by distance from centre
    stations_within_r = [] # Create an empty list of stations for the function to return
    
    for i in station_dist:
        if i[1] <= r: stations_within_r.append(i[0])
        else: break # Break the loop early, since the list is sorted by distance

    return stations_within_r


def rivers_with_station(stations):
    """This function takes a list of MonitorinStation objects, returning a set of the names of rivers with a monitoring station."""

    return set([i.river for i in stations]) # Rieturn a set of the names of rivers wth a monitoring station


def stations_by_river(stations):
    """This function takes a list of MonitoringStation objects, returning a dictionary that maps river names to a list of stations on that river."""

    river_to_stations = {key : [] for key in rivers_with_station(stations)} # Create an dictionary with river names as keys and empty lists as values
    
    # Append stations to their respective river lists
    for i in stations:
        river_to_stations[i.river].append(i)

    return river_to_stations


#task E#
def rivers_by_station_number(stations, N):
    river_and_nstation=[]
    nstation_by_river =  stations_by_river(stations)
    for i in station_by_river:
        nstation=len(station_by_river[i])
        station_per_river=i,nstation
        nstation_by_river.append(station_per_river)
    sorted_nstation_by_river=sorted_by_key(nstation_by_river,1,reverse=True)

    if sorted_nstation_by_river[N][1]==sorted_nstation_by_river[N+1][1]:
        n=0
        while sorted_nstation_by_river[N][1]==sorted_nstation_by_river[N+n+1][1]:
            n+=1
        return sorted_nstation_by_river[:N+n]
    else:
        return sorted_nstation_by_river[N]

#task F

                
