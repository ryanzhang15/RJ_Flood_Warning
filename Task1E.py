from floodsystem.stationdata import build_station_list

def run():

    # Build list of stations
    stations = build_station_list()
    list_of_rivers_numbers=rivers_by_station_number(stations, 9)


