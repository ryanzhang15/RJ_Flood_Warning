# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT

import datetime
from floodsystem.analysis import analyze_risk, polyfit
from floodsystem.stationdata import build_station_list

def test_polyfit():
    dates = [datetime.datetime.now()-datetime.timedelta(days=i) for i in range(10)]
    levels = [3, 5]
    p = 4

    a, b = polyfit(dates, levels, p)
    
    assert a
    assert b


def test_analyze_risk(stations):
    stations = build_station_list()
    stations_risk = analyze_risk(stations)

    assert stations_risk
    assert len(stations_risk) <= len(stations)
    
    for _, b in stations_risk:
        assert b in ["low", "moderate", "high", "severe"]