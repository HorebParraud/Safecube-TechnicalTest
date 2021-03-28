#! /usr/bin/python3

import pytest
import sources.trackpoints as script


class TestTrackpoint:

    # - dictionary samples provided to the class
    DATA =  [
        {"data": {"mac1": "4C:77:6D:FA:EF:60", "mac2": "4C:77:6D:FA:EF:61", "type": "Wifi", "geoloc": False}, "radius": 131, "is_done": True, "latitude": 49.3517125, "longitude": 2.762460709, "date_reached": "2021-01-20 16:52"},
        {"data": {"mac1": "4C:77:6D:F8:0C:E5", "mac2": "00:3A:9A:69:F5:50", "type": "Wifi", "geoloc": False}, "radius": 147, "is_done": True, "latitude": 49.3521656, "longitude": 2.762288571, "date_reached": "2021-01-20 17:02"},
        {"data": {"mac1": "34:FA:9F:2F:11:58", "mac2": "EC:AD:E0:EC:3D:63", "type": "Wifi", "geoloc": False}, "radius": 84, "is_done": True, "latitude": 48.8660382, "longitude": 2.334203008, "date_reached": "2021-01-22 01:07"},
        {"data": {"mac1": "34:FA:9F:2F:11:58", "mac2": "EC:AD:E0:EC:3D:63", "type": "Wifi", "geoloc": False}, "radius": 84, "is_done": True, "latitude": 48.8660382, "longitude": 2.334203008, "date_reached": "2021-01-22 12:07"}
    ]

    # - initialization of the class, filling with 4 data dctionaries provided
    #   in the disorder
    def setup_method(self):
        self.trackeds = script.Trackpoints(2, 12)

        self.trackeds.append(self.DATA[3])
        self.trackeds.append(self.DATA[2])
        self.trackeds.append(self.DATA[1])
        self.trackeds.append(self.DATA[0])

    # - redefinition of the maximum area for a stop
    def test_track_stopscope(self):
        self.trackeds.set_stopscope(4)
        assert self.trackeds.get_stopscope() == 4

    # - definition of minimum time (in hours)
    def test_track_stoptime(self):
        self.trackeds.set_scopetime(24)
        assert self.trackeds.get_stopstime() == float(24)

    # - verification of the number of dealers in the list
    def test_track_appenddata(self):
        assert len(self.trackeds.get_trackpoint()) == 4

    # - check that the dictionaries have been sorted in the list
    def test_track_sortdata(self):
        assert self.trackeds.get_trackpoint()[0]['date_reached'] < self.trackeds.get_trackpoint()[1]['date_reached']

    # - compare the distance between two dictionaries
    def test_comparet_twopos(self):
        comput = self.trackeds.compare_twopointscope(0, 1)
        assert comput[0] == True and comput[1] == 0.051902419153737965

    # - compare the time between two dictionaries based on their 'date' values
    def test_comparet_twotime(self):
        comput = self.trackeds.compare_twopointtime(0, 1)
        assert comput[0] == False and comput[1] == 600.0

    # - determining the stops in the dictionary list
    def test_findstop_indictionnary(self):
        self.trackeds.findstop(0)