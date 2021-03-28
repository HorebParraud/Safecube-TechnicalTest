#!/usr/bin/env python3

from haversine import haversine, Unit
from datetime import datetime
from sources import stop


class Trackpoints():
    def __init__(self, scope, time):
        self.__stopscope = float(scope)
        self.__stoptime = time * 3600
        self.__stop = []
        self.__tp = []

    def print_tracked_point(self):
        for x in self.__tp:
            print(x)

    def print_finded_stop(self):
        for x in self.__stop:
            print("Stop :")
            print(x.get_info())

    # - [DEBUG] display data compare point by point
    def printlog(self, index):
        for x in range(index + 1, len(self.__tp)):
            print(f'{index} - {x}\t{self.compare_twopointtime(index, x)}'
                + f' - {self.compare_twopointscope(index, x)}')
            index += 1

    def get_trackpoint(self):
        return self.__tp

    # - return scope in km
    def get_stopscope(self):
        return self.__stopscope

    # - return converting timestamp to hour
    def get_stopstime(self):
        return self.__stoptime / 3600

    # - defines the area in kilometres of radius that defines a point
    #   accumulation as a stop
    def set_stopscope(self, scope):
        self.__stopscope = scope

    # - defines the minimum time before point accumulation is considered as a
    #   stop (given in hours, converted to timestamp)
    def set_scopetime(self, time):
        self.__stoptime = time * 3600

    # - add a dictionary at the end of the point list __tp
    # - sort the dictionary list by "date_reached" in __tp
    def append(self, tp):
        self.__tp.append(tp)
        self.__tp.sort(key=lambda i: (i['date_reached']))

    # - creation of a Stop object from the two indexes retrieved in findstop()
    # - compute time's stop use the compare_twopointtime() function to avoid
    #   copying the function into the Stop class
    # - add this new object Stop to the __stop list
    def __appendstop(self, index, t):
        time = self.compare_twopointtime(index, t)[1]

        self.__stop.append(stop.Stop(self.__tp[index], self.__tp[t], time))

    # - determining the distance (in km) between two points in the list
    def compare_twopointscope(self, index1, index2):
        p1 = (self.__tp[index1]['latitude'], self.__tp[index1]['longitude'])
        p2 = (self.__tp[index2]['latitude'], self.__tp[index2]['longitude'])
        distance = haversine(p1, p2)

        return [distance <= self.__stopscope, distance]

    # - converting dates to timestamp is a good way to compare two times date
    def compare_twopointtime(self, index1, index2):
        d_r = 'date_reached'
        fmt = "%Y-%m-%d %H:%M"
        d1 = datetime.timestamp(datetime.strptime(self.__tp[index1][d_r], fmt))
        d2 = datetime.timestamp(datetime.strptime(self.__tp[index2][d_r], fmt))

        return [(d2 - d1) >= self.__stoptime, d2 - d1]

    # - recursive stop detection algorithms to the stolen defined by the
    #   stopscope and stoptime rules
    def findstop(self, index):
        for t in range(index + 1, len(self.__tp)):
            cmp_km = self.compare_twopointscope(index, t)
            cmp_tm = self.compare_twopointtime(index, t)

            # [DEBUG] print itération and step of the function
            # print(f'{index} - {t} : {cmp_tm} - {cmp_km}')

            # - the points show that the carrier is not in a state of rest.
            #   reiteration from the following points
            if cmp_tm[0] is False and cmp_km[0] is False:
                # print('Time Fasle - Km False\n')
                self.findstop(t)
                break
            # - the points are in the same area: continuing the loop allows to
            #   check with the next point(s) (further away in time) if the
            #   vehicle stays in this area long enough
            #   to be considered as a stop
            elif cmp_tm[0] is False and cmp_km[0] is True:
                # print('Time False - Km True')
                continue
            # - This (rare) case is detailed here (half of the condition is
            #   enough to handle two cases) for better readability
            #   and maintainability of the code
            elif cmp_tm[0] is True and cmp_km[0] is False:
                # print('Time True - Km False')
                self.findstop(t)
                break
            # - dots prove a stop state. add dictionary references to create a
            #   stop object, reiterate algorithms to check the rest of the list
            else:
                # print('Time True - Km True\n')
                self.__appendstop(index, t)
                self.findstop(t)
                break
