Weather Underground PWS Python API
==================================

A small Python module for [Weather Underground PWS](https://www.wunderground.com/weatherstation/hardwareandsoftware.asp)
APIs.

### Installation

    $ pip3 install wunderground_pws

### Example usage

```python
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
```

### Building docs

    $ pip3 install -r requirements-docs.txt
    $ cd docs/
    $ make html
