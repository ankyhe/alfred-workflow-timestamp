#! /usr/bin/env python

import calendar
from datetime import datetime
from display import Display
import sys
import os

def dt2ts(dt):
    return calendar.timegm(dt.utctimetuple())


now = dt2ts(datetime.utcnow())
use_milli_global = False if 'USE_SECONDS_AS_DEF' in os.environ else True

def add_time(ts, hours, ts_title, display, use_milli = use_milli_global):
    used_ts = ts + hours * 3600
    used_ts_str = str(int(used_ts * 1000)) if use_milli else str(int(used_ts))
    used_ts_human_str = datetime.utcfromtimestamp(used_ts).strftime('UTC: %Y-%m-%d %H:%M:%S')
    display.add_item(title = '{0} - {1}'.format(ts_title, used_ts_str),
            subtitle = used_ts_human_str,
            valid = 'yes',
            arg = used_ts_str,
            icon = 'icon.png')

def add_align_time(ts, hours, ts_title, display, use_milli = use_milli_global):
    new_ts = (ts + hours * 3600)
    # align_ts is 00:00:00
    align_ts = new_ts - new_ts % (24 * 3600)
    used_ts = str(int(align_ts * 1000)) if use_milli else str(int(align_ts))
    used_ts_human_str = datetime.utcfromtimestamp(align_ts).strftime('UTC: %Y-%m-%d %H:%M:%S')
    display.add_item(title = '{0} - {1}'.format(ts_title, used_ts),
            subtitle = used_ts_human_str,
            valid = 'YES',
            arg = used_ts,
            icon = 'icon.png')

if len(sys.argv) == 1:
    display = Display()
    add_time(now, 0, 'now', display)
    add_align_time(now, 0, 'today 00:00', display)
    add_time(now, -24, '-24h', display)
    add_align_time(now, -24, '-1d 00:00', display)
    add_time(now, -24 * 7, '-7d', display)
    add_align_time(now, -24 * 7, '-7d 00:00', display)
    add_time(now, -24 * 30, '-30d', display)
    add_align_time(now, -24 * 30, '-30d 00:00', display)
    add_time(now, -24 * 90, '-90d', display)
    add_align_time(now, -24 * 90, '-90d 00:00', display)
    print(display)
else:
    display = Display()
    datetime_str = sys.argv[1]
    if datetime_str.find('T') == -1:
        datetime_str = '{0}T00:00:00'.format(datetime_str)
    if len(datetime_str.split(':')) < 2:
        datetime_str = '{0}:00:00'.format(datetime_str)
    elif len(datetime_str.split(':')) < 3:
        datetime_str = '{0}:00'.format(datetime_str)
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
    datetime_ts = dt2ts(datetime_obj)
    add_time(datetime_ts, 0, datetime_str, display, True)
    add_time(datetime_ts, 0, datetime_str, display, False)
    print(display)
