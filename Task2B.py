# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list() # Build list of stations
    update_water_levels(stations) # Update water levels
    stations_level = stations_level_over_threshold(stations, 0.8) # Find stations with relative water level over 0.8
    for i in stations_level:
        print(i[0].name, i[1])


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
