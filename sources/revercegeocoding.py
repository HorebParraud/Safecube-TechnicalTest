#!/usr/bin/env python3

import requests
import json
import logging
from requests_oauthlib import OAuth1

# - connect to https://developer.here.com/projects/ to generate an id and a
#   private key for communication to the api
HERE_CLIENT_ID = "8GA4mqGrA7WEerLtk1PP7g"
HERE_CLIENT_SECRET = "l4o6ucLjGJuHkuvS6YFGC-il04aZdJJ9ggkTWDOCWsa_-_RqzFKd7oH-ZGbCJJZqQ84jV8SCVjcIgOEI86nNJw"


# - function retrieving by an api call the data relative to a GPS position
def fetch_reversegeocoding(lat, lng):
    # - body of request
    data = {
        "grantType": "client_credentials",
        "clientId": HERE_CLIENT_ID,
        "clientSecret": HERE_CLIENT_SECRET,
    }

    # - 0auth request of connection
    response = requests.post(
        url="https://account.api.here.com/oauth2/token",
        auth=OAuth1(HERE_CLIENT_ID, client_secret=HERE_CLIENT_SECRET),
        headers={"Content-type": "application/json"},
        data=json.dumps(data),
    ).json()

    # - Oauth request to get the tokens needed to communicate with the API
    token = response["accessToken"]
    token_type = response["tokenType"]

    headers = {"Authorization": f"{token_type} {token}"}
    resp = requests.get(
        f"https://revgeocode.search.hereapi.com/v1/revgeocode?at={lat}%2C{lng}&lang=en-US",
        headers=headers,
    )

    # - Error handling
    logging.debug(f"Response {resp.status_code}:{resp}")
    if not resp.status_code == 200:
        return

    payload = resp.json()
    if len(payload.get("items", [])) and payload["items"][0].get("address"):
        return payload["items"][0]["address"]