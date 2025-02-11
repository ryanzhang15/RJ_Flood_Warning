import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from .analysis import polyfit

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")

    plt.xticks(rotation = 45)
    plt.title("Station {}".format(station.name))

    low = station.typical_range[0]
    high = station.typical_range[1]

    low_x = np.ones(len(dates)) * low
    high_x = np.ones(len(dates)) * high

    plt.plot(dates, low_x, label="Typical low")
    plt.plot(dates, high_x, label="Typical high")

    plt.legend()
    plt.tight_layout()
    plt.show()
    return

def plot_water_level_with_fit(station, dates, levels, p):
    """This function plots water levels, with a polynomial fit."""

    plt.plot(dates, levels, label="Actual water levels")
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")

    plt.xticks(rotation = 45);
    plt.title("Station {}".format(station.name))

    low = station.typical_range[0]
    high = station.typical_range[1]

    low_x = np.ones(len(dates)) * low
    high_x = np.ones(len(dates)) * high

    plt.plot(dates, low_x)
    plt.plot(dates, high_x)

    # Fit a polynomial of degree p to the data
    poly, shift = polyfit(dates, levels, p)

    # Shift dates back
    num_dates = matplotlib.dates.date2num(dates)
    x = np.linspace(num_dates[0], num_dates[-1], 1000)

    plt.plot(x, poly(x + shift), label="Polynomial fit for water levels")

    plt.legend()
    plt.tight_layout()
    plt.show()

