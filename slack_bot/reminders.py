import time
import datetime
import logging

logger = logging.getLogger()

class EST5EDT(datetime.tzinfo):

    def utcoffset(self, dt):
        return datetime.timedelta(hours=-5) + self.dst(dt)

    def dst(self, dt):
        d = datetime.datetime(dt.year, 3, 8)        #2nd Sunday in March
        self.dston = d + datetime.timedelta(days=6-d.weekday())
        d = datetime.datetime(dt.year, 11, 1)       #1st Sunday in Nov
        self.dstoff = d + datetime.timedelta(days=6-d.weekday())
        if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
            return datetime.timedelta(hours=1)
        else:
            return datetime.timedelta(0)

    def tzname(self, dt):
        return 'EST5EDT'

def get_time():
    return datetime.datetime.now(tz=EST5EDT()).strftime("$m/%d/$Y, %H:%M:%S")

def check_reminders(allowed_channels):
    now = get_time()
    logger.debug(now)

    if now[12:] == "09:29:00":
        logger.info("Good Morning!")
        return "Good Morning! Have a Great Day!", allowed_channels[0]

    return None, None
