#! /usr/bin/env python

from datetime import datetime, tzinfo, timedelta
from display import Display
import sys
import time

FORMAT = '%Y-%m-%d %H:%M:%S %z'
FORMAT_WITHOUT_TZINFO = '%Y-%m-%d %H:%M:%S %z'


class LocalTZ(tzinfo):
    _unixEpochOrdinal = datetime.utcfromtimestamp(0).toordinal()

    def dst(self, dt):
        return timedelta(0)

    def utcoffset(self, dt):
        t = (dt.toordinal() - self._unixEpochOrdinal) * 86400 + dt.hour * 3600 + dt.minute * 60 + dt.second + time.timezone
        utc = datetime(*time.gmtime(t)[:6])
        local = datetime(*time.localtime(t)[:6])
        return local - utc


def timestamp_to_str(ts):
    used_ts = int(ts)
    if len(str(ts)) == len('1545730073000'):
        used_ts = int(ts) / 1000
    utc_datetime = datetime.utcfromtimestamp(used_ts)
    local_datetime = datetime.fromtimestamp(used_ts)
    local_datetime = local_datetime.replace(tzinfo = LocalTZ())
    return utc_datetime, local_datetime


if len(sys.argv) > 1:
    ts = sys.argv[1]
    utc_datetime, local_datetime = timestamp_to_str(ts)
    display = Display()
    display.add_item(title = '{0} - {1} {2}'.format(ts, 'UTC', utc_datetime.strftime(FORMAT_WITHOUT_TZINFO)),
            valid = 'YES', 
            arg = utc_datetime.strftime(FORMAT_WITHOUT_TZINFO),
            icon = 'icon.png')
    display.add_item(title = '{0} - {1} {2}'.format(ts, 'Local', local_datetime.strftime(FORMAT)),
            valid = 'YES', 
            arg = local_datetime.strftime(FORMAT_WITHOUT_TZINFO),
            icon = 'icon.png')
    print(display)
