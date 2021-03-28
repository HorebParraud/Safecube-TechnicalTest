#! /usr/bin/python3

import pytest
import sources.revercegeocoding as script

# - function retrieving by an api call the data relative to a GPS position
def test_reverce_geocogin():
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
    assert script.fetch_reversegeocoding(48.8660382, 2.334203008) == tmp

def test_reverce_geocogin_bad_argument():
    assert script.fetch_reversegeocoding(0.4, 0.4) is None