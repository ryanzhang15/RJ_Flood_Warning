# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to water level analysis.

"""

import matplotlib
import matplotlib.dates
import numpy as np

from .flood import stations_level_over_threshold
from .stationdata import update_water_levels

def polyfit(dates, levels, p):
    """This function takes a list of dates, a list of water levels, and an integer p, returning a tuple of (polynomial of degree p, shift of time axis) that fits the data best according to least squares."""

    x = matplotlib.dates.date2num(dates)
    y = np.array(levels)

    coeff = np.polyfit(x - x[0], y, p) # Fit a polynomial of degree p to the data. Note data is shifted left by x[0] to avoid numerical instability with higher order polynomials

    return np.poly1d(coeff), -x[0] # Return the polynomial and the shift of the time axis


def analyze_risk(stations):
    """This function takes a list of MonitoringStation objects, returning a list of (MonitoringStation, string) tuples describing the risk either as "severe", "high", "moderate", or "low"."""

    update_water_levels(stations) # Update the water levels of the stations, also to get relative water levels
    station_level = stations_level_over_threshold(stations, -1) # Retrieve all stations with relative water levels
    station_risk = [] # Create an empty list of tuples to store station and risk

    for station, level in station_level:
        if level < 0.9: pass #assume no flooding risk
        elif level < 1.2: station_risk.append((station, "low"))
        elif level < 1.7: station_risk.append((station, "moderate"))
        elif level < 2.2: station_risk.append((station, "high"))
        else: station_risk.append((station, "severe"))
                                  
    return station_risk
        