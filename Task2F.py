from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit

import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations_relative = stations_highest_rel_level(stations, 5)

    d = 2

    for station in stations_relative:
        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=d))
        plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == '__main__':
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()