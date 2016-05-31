# Geocoord for Python

## What is Geocoord for Python

Geocoord for Python is python library for you get geographic coordinates values from locations database in your python application.

## Get started

### Installation

You can install Geocoord for Python via pip command.

```bash
$ pip install geocoord
```

### How to use

You can use Geocoord for Python in your application.

```bash
$ python
Python 2.7.11+ (default, Apr 17 2016, 14:00:29) 
[GCC 5.3.1 20160413] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from geocoord.search import Search
>>> s = Search()
>>> s.find_coord_by_city('sapporo')
{'lat': 43.06417, 'lon': 141.34694}
```
