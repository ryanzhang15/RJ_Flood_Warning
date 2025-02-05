# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT

from floodsystem.analysis import analyze_risk
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    stations_risk = analyze_risk(stations)

    print("Stations with flooding risk:")
    for station, risk in stations_risk:
        print(station.name, risk)

if __name__ == '__main__':
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()