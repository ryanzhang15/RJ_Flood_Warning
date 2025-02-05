# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT

from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list() # Build list of stations
    update_water_levels(stations) # Update water levels
    stations_level = stations_highest_rel_level(stations, 100)
    for i in stations_level:
        print(i.name, i.relative_water_level())


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
