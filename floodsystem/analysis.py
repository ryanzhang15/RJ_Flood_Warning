# Copyright (C) 2025 Ryan J Zhang
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to water level analysis.

"""

import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    """This function takes a list of dates, a list of water levels, and an integer p, returning a tuple of (polynomial of degree p, shift of time axis) that fits the data best according to least squares."""

    x = matplotlib.dates.date2num(dates)
    y = np.array(levels)

    coeff = np.polyfit(x - x[0], y, p) # Fit a polynomial of degree p to the data. Note data is shifted left by x[0] to avoid numerical instability with higher order polynomials

    return np.poly1d(coeff), -x[0] # Return the polynomial and the shift of the time axis