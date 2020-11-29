# This file is a part of WUnderground PWS Python API
# Copyright (c) 2019 Marco Aceti <mail@marcoaceti.it>
# See LICENSE file for more details about licensing and copying.


import datetime
import simplejson

import requests

from .exceptions import *
from . import units


class WUndergroundAPI:
    """

    """
    _base_url = 'https://api.weather.com/v2/'

    def __init__(self, api_key: str,
                 default_station_id: str = None,
                 units: str = units.METRIC_SI_UNITS,
                 fmt: str = 'json'):
        """Creates a new WUndergroundAPI object

        :param str api_key: A valid Weather Underground API key, obtained by Settings gear > Member settings > API keys
        :param str default_station_id: Default station ID. \
        Can be None, if not specified you must pass it every time you use PWS methods
        :param str units: The unit of measure for the response. The following values are supported: \
        `wundeground_pws.ENGLISH_UNITS`, `wundeground_pws.METRIC_UNITS`,\
        `wundeground_pws.HYBRID_UNITS`, `wundeground_pws.METRIC_SI_UNITS`
        :param str fmt: Response format, can be json or xml
        """
        self.api_key = api_key
        self.default_station_id = default_station_id
        self.units = units
        self.fmt = fmt

    def _request(self, path: tuple, **kwargs):
        """Forward a raw request to Weather Underground APIs"""
        r = requests.get(self._base_url + '/'.join(path), params={
            'apiKey': self.api_key,
            'units': self.units,
            'format': self.fmt,
            'numericPrecision': 'decimal',
            **kwargs
        })
        if r.status_code != 200:
            try:
                raise BadRequestError(r.json()['errors'])
            except (simplejson.errors.JSONDecodeError, KeyError):
                raise BadRequestError(r.text)
        return r.json()

    def current(self, station_id: str = None):
        """Get the current status of a PWS

        :param station_id: The target station ID. This overrides the default setting if already specified
        :type station_id: str
        :returns: The current conditions observations for the current record
        :rtype: dict
        :raises:
            - :class:`.exceptions.StationIDNotSuppliedError`
            - :class:`.exceptions.BadRequestError`
        """
        if not self.default_station_id and not station_id:
            raise StationIDNotSuppliedError("You must supply a station ID in __init__() "
                                            "or fill the station_id parameter in every method!")

        return self._request(('pws', 'observations', 'current'),
                             stationId=station_id or self.default_station_id)

    def hourly(self, station_id: str = None):
        """Get the latest 7 days observations history of a PWS

        :param station_id: he target station ID. This overrides the default setting if already specified
        :type station_id: str
        :returns: The hourly records for the latest 7 days of observations
        :rtype: dict
        :raises:
            - :class:`.exceptions.StationIDNotSuppliedError`
            - :class:`.exceptions.BadRequestError`
        """
        if not self.default_station_id and not station_id:
            raise StationIDNotSuppliedError("You must supply a station ID in __init__() "
                                            "or fill the station_id parameter in every method!")

        return self._request(('pws', 'observations', 'hourly', '7day'),
                             stationId=station_id or self.default_station_id)

    def summary(self, station_id: str = None):
        """Get the latest 7 days observations summaries of a PWS

        :param station_id: The target station ID. This overrides the default setting if already specified
        :type station_id: str
        :return: The daily summary of daily observations for the latest 7 days
        :rtype: dict
        :raises:
            - :class:`.exceptions.StationIDNotSuppliedError`
            - :class:`.exceptions.BadRequestError`
        """
        if not self.default_station_id and not station_id:
            raise StationIDNotSuppliedError("You must supply a station ID in __init__() "
                                            "or fill the station_id parameter in every method!")

        return self._request(('pws', 'dailysummary', '7day'),
                             stationId=station_id or self.default_station_id)

    def history(self, date: datetime.date, granularity: str = 'hourly', station_id: str = None):
        """Get history for a given day

        :param date: Request a specific date
        :type date: datetime.date
        :param granularity: Specify the granularity of the results. Possible values: hourly, daily or all.
        :type granularity: str
        :param station_id: The target station ID. This overrides the default setting if already specified
        :type station_id: str
        :return: History of the specified time
        :rtype: dict
        :raises:
            - :class:`.exceptions.StationIDNotSuppliedError`
            - :class:`.exceptions.BadRequestError`
        """
        if not self.default_station_id and not station_id:
            raise StationIDNotSuppliedError("You must supply a station ID in __init__() "
                                            "or fill the station_id parameter in every method!")

        return self._request(('pws', 'history', granularity),
                             date=date.strftime("%Y%m%d"),
                             stationId=station_id or self.default_station_id)
