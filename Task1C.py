# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""

    stations = build_station_list() # Build list of stations

    p = (52.2053, 0.1218) # Define coordinate of Cambridge city centre, as specified
    r = 10 # Define radius of 10km

    stations_within_r = [i.name for i in stations_within_radius(stations, p, r)] # Extract name of stations within radius

    print("Stations within 10km of Cambridge city centre:")
    print(sorted(stations_within_r))
    

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run() 
    