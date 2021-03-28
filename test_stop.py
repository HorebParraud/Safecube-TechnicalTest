#! /usr/bin/python3

import pytest
import json
import sources.stop as script


class TestStop:

    # - dictionary samples provided to the class
    DATA =  [
        {"data": {"mac1": "34:FA:9F:2F:11:58", "mac2": "EC:AD:E0:EC:3D:63", "type": "Wifi", "geoloc": False}, "radius": 84, "is_done": True, "latitude": 48.8660382, "longitude": 2.334203008, "date_reached": "2021-01-22 01:07"},
        {"data": {"mac1": "34:FA:9F:2F:11:58", "mac2": "EC:AD:E0:EC:3D:63", "type": "Wifi", "geoloc": False}, "radius": 84, "is_done": True, "latitude": 48.8660382, "longitude": 2.334203008, "date_reached": "2021-01-22 12:07"}
    ]

    # - initialize the class with a data pair
    def setup_method(self):
        self.stop = script.Stop(self.DATA[0], self.DATA[1], 43200)

    # - dictionary retrieval "startofstop"
    def test_startofstop(self):
        assert self.stop.get_startofstop() == self.DATA[0]

    # - dictionary retrieval "endofstop"
    def test_endofstop(self):
        assert self.stop.get_endofstop() == self.DATA[1]

    # - recovery of stopping time of the vehicle for the stop
    def test_durationofstop(self):
        assert self.stop.get_duration() == 43200

    # - retrieve information related to the fonction fetch_reversegeocoding
    def test_stop_info(self):
        tmp = {
            'label': "19 Avenue de l'Opéra, 75001 Paris, France",
            'countryCode': 'FRA',
            'countryName': 'France',
            'stateCode': 'IDF',
            'state': 'Ile-de-France',
            'county': 'Paris',
            'city': 'Paris',
            'district': '1er Arrondissement',
            'street': "Avenue de l'Opéra",
            'postalCode': '75001',
            'houseNumber': '19'
        }
        assert self.stop.get_info()['place'] == tmp