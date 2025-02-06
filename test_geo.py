# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT


from floodsystem.geo import rivers_by_station_number, stations_by_river, stations_within_radius
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit


def test_stations_within_radius():

    stations = build_station_list()

    centre = (52.2053, 0.1218)
    r = 10

    stations_within_r = stations_within_radius(stations, centre, r)
    
    assert stations_within_r


    for i in stations_within_r:
        dist = haversine(i.coord, centre, unit=Unit.KILOMETERS)
        assert dist <= r


def test_stations_by_river():

    stations = build_station_list()

    river_to_stations = stations_by_river(stations)

    assert river_to_stations

    for i in river_to_stations:
        assert river_to_stations[i]
    

def test_rivers_by_station_number():

    stations = build_station_list()

    N = 10

    rivers = rivers_by_station_number(stations, N)

    assert rivers

    for a, b in rivers:
        assert a
        assert b