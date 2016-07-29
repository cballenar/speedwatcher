# SpeedWatcher
Takes logged internet speeds from a database and returns summary based on period of time.

## Usage
````python
from speedwatcher import SpeedWatcher

x = SpeedWatcher('2016-04-06 00:00:00', '2016-07-06 23:59:59')

hh = x.get_data('ping', 'hour')        # hour by default
dd = x.get_data('speed_up', 'day')
ww = x.get_data('speed_down', 'week')
mm = x.get_data('speed_down', 'month')

for row in ww:
    print row

'{"data": 5.03, "time": "2016-04-07 03:00:00"}'
'{"data": 4.81, "time": "2016-04-11 00:00:00"}'
'{"data": 5.19, "time": "2016-04-18 00:00:00"}'
'{"data": 5.19, "time": "2016-04-25 00:00:00"}'
'{"data": 5.51, "time": "2016-05-02 00:00:00"}'
'{"data": 4.56, "time": "2016-05-09 00:00:00"}'
'{"data": 4.42, "time": "2016-05-16 00:00:00"}'
'{"data": 4.63, "time": "2016-05-23 00:00:00"}'
'{"data": 3.14, "time": "2016-05-30 00:00:00"}'
'{"data": 2.62, "time": "2016-06-06 00:00:00"}'
'{"data": 2.17, "time": "2016-06-13 00:00:00"}'
'{"data": 1.48, "time": "2016-06-20 00:00:00"}'
'{"data": 1.85, "time": "2016-06-27 00:00:00"}'
'{"data": NaN, "time": "2016-07-04 00:00:00"}'
````