# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Requirements for Task 1D"""

    stations = build_station_list() # Build list of stations

    rivers = rivers_with_station(stations) # Get a set of rivers with a monitoring station

    # Print data for rivers
    print("River data:")
    print(f"{len(rivers)} stations. First 10 - {list(rivers)[:10]}")

    # Print detailed station data for specific rivers
    river_to_station = stations_by_river(stations) # Get a dictionary of rivers to stations

    print("River Aire:")
    print(sorted([i.name for i in river_to_station["River Aire"]]))
    
    print("River Cam:")
    print(sorted([i.name for i in river_to_station["River Cam"]]))
    
    print("River Thames:")
    print(sorted([i.name for i in river_to_station["River Thames"]]))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run() 
    