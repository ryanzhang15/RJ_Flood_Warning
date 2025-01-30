# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    stations = build_station_list() # Build list of stations

    p = (52.2053, 0.1218) # Define coordinate of Cambridge city centre, as specified

    # Get a list of (station, distance) tuples sorted by distance from p
    station_dist = stations_by_distance(stations, p)

    closest, furthest = [], []

    # Find the closest 10 entries
    for i in station_dist[:10]:
        closest.append((i[0].name, i[0].town, i[1]))

    # Find the furthest 10 entries
    for i in station_dist[-10:]:
        furthest.append((i[0].name, i[0].town, i[1]))

    print("Closest 10 stations to Cambridge city centre:")
    print(closest)
    print("Furthest 10 stations from Cambridge city centre:")
    print(furthest)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run() 
    