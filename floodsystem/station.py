# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    #task F
    def typical_range_consistent(self):
        # Consistent if data exists, and high is larger than or equal to low
        return self.typical_range is not None and float(self.typical_range[1]) >= float(self.typical_range[0]) 
    
    # task 2B
    def relative_water_level(self):
        if not self.typical_range_consistent() or self.latest_level is None:
            return None
        else:
            return (self.latest_level - self.typical_range[0])/(self.typical_range[1] - self.typical_range[0])


#also task F
def inconsistent_typical_range_stations(stations):
    '''This function takes a list of MonitoringStation objects, returning a list of names of stations with inconsistent typical low/high ranges.'''

    incon_tr_station=[]
    for i in stations:
        if i.typical_range_consistent()==False:
            incon_tr_station.append(i.name)
    return sorted(incon_tr_station) # Return sorted stations



