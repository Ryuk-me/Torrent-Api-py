import time


def getUptime(startTime: time) -> time:
    """
    Returns the number of seconds since the program started.
    """
    return time.time() - startTime
