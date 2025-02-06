# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT

from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list


def test_stations_level_over_threshold():

    stations = build_station_list()
    tol = 0.8

    stations_level = stations_level_over_threshold(stations, tol)

    assert stations_level

    for a, b in stations_level:
        assert a
        assert b > tol


def test_stations_highest_rel_level():

    stations = build_station_list()
    N = 10

    stations_highest = stations_highest_rel_level(stations, N)

    assert len(stations_highest) == N
