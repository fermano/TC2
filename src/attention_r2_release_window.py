from datetime import datetime
def within_release_window(timestamp: datetime, start: datetime, end: datetime) -> bool:
    return start <= timestamp < end
