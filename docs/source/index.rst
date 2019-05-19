.. WUnderground PWS API documentation master file, created by
   sphinx-quickstart on Sun May 19 17:39:51 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Weather Underground PWS Python API's documentation
==================================================

A small Python module for `Weather Underground PWS <https://www.wunderground.com/weatherstation/hardwareandsoftware.asp>`_ API.

Example::

   from datetime import date
   from pprint import pprint

   from wunderground_pws import WUndergroundAPI, units

   wu = WUndergroundAPI(
      api_key='my api key',
      default_station_id='KMAHANOV10',
      units=units.ENGLISH_UNITS,
   )
   print('Current status of my weather station:')
   pprint(wu.current()['observations'][0])
   print('Summary of last 7 days:')
   pprint(wu.summary())
   print('Detailed hourly history for the last 7 days:')
   pprint(wu.hourly())
   print('History for 4/20/2019:')
   pprint(wu.history(date(day=20, month=4, year=2019)))


Installation
************

You can install this module by using pip::

   $ pip3 install wunderground_pws


WUndergroundAPI class
*********************

.. automodule:: wunderground_pws
   :members: WUndergroundAPI

Common exceptions
*****************

.. automodule:: wunderground_pws.exceptions
   :members: BadRequestError, StationIDNotSuppliedError

.. toctree::
   :maxdepth: 2
   :caption: Contents:
