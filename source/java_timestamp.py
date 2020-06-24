#! /usr/bin/env python

import calendar
from datetime import datetime
from display import Display

def dt2ts(dt):
    return calendar.timegm(dt.utctimetuple())

display = Display()
now = dt2ts(datetime.utcnow())

def add_time(ts, hours, ts_title):
    used_ts = ts + hours * 3600
    used_ts_str = str(int(used_ts * 1000))
    used_ts_human_str = datetime.utcfromtimestamp(used_ts).strftime('%Y-%m-%d %H:%M:%S')
    display.add_item(title = '{0} - {1}'.format(ts_title, used_ts_str),
            subtitle = used_ts_human_str,
            valid = 'yes',
            arg = used_ts_str,
            icon = 'icon.png')
    return display

def add_align_time(ts, hours, ts_title):
    new_ts = (ts + hours * 3600)
    # align_ts is 00:00:00
    align_ts = new_ts - new_ts % (24 * 3600)
    used_ts = str(int(align_ts * 1000))
    used_ts_human_str = datetime.utcfromtimestamp(align_ts).strftime('%Y-%m-%d %H:%M:%S')
    display.add_item(title = '{0} - {1}'.format(ts_title, used_ts),
            subtitle = used_ts_human_str,
            valid = 'YES',
            arg = used_ts,
            icon = 'icon.png')
    return display

add_time(now, 0, 'now')
add_align_time(now, 0, 'today 00:00')
add_time(now, -24, '-24h')
add_align_time(now, -24, '-1d 00:00')
add_time(now, -24 * 7, '-7d')
add_align_time(now, -24 * 7, '-7d 00:00')
add_time(now, -24 * 30, '-30d')
add_align_time(now, -24 * 30, '-30d 00:00')
add_time(now, -24 * 90, '-90d')
add_align_time(now, -24 * 90, '-90d 00:00')

print display

