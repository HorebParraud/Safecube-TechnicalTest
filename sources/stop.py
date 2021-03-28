#! /usr/bin/python3

from sources import revercegeocoding

class Stop():
    def __init__(self, startofstop, endofstop, duration):
        self.__startofstop = startofstop
        self.__endofstop = endofstop
        self.__duration = duration
        self.__buf = revercegeocoding.fetch_reversegeocoding(
                        self.__startofstop['latitude'],
                        self.__startofstop['longitude'])

        # - creation of a json file containing the important information of the
        #   trackers point, as well as several information on the time and the
        #   approximate place of the stop
        self.__info = {
            "mac1": self.__startofstop['data']['mac1'],
            "mac2": self.__startofstop['data']['mac2'],
            "latitude": self.__startofstop['latitude'],
            "longitude": self.__startofstop['longitude'],
            "startDate": self.__startofstop['date_reached'],
            "endDate": self.__endofstop['date_reached'],
            "duration": self.__duration,
            "place": self.__buf
        }

    def get_startofstop(self):
        return self.__startofstop

    def get_endofstop(self):
        return self.__endofstop

    def get_duration(self):
        return self.__duration

    def get_info(self):
        return self.__info

