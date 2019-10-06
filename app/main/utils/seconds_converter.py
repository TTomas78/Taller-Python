import datetime


def seconds_to_time(seconds):
    """:param seconds: seconds we want to convert
       :type seconds: int
       :rtype: datetime.time object
       >>> seconds-to-time(3600)
       datetime.time(hour=1,minute=0,second=0)
    """
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60

    return datetime.time(hour, minutes, seconds)


def time_to_seconds(time):
    """:param time: time we want to convert
        :type time: datetime.time
        :rtype: int
        >>> time_to_seconds(datetime.time(hour=1,minute=1,second=30))
        3690
    """
    hours_in_seconds = time.hour * 3600
    minutes_in_secods = time.minute * 60
    return hours_in_seconds + minutes_in_secods + time.second
