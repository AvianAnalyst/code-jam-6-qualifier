import datetime


def validate_date(date: str) -> None:
    date_sections = date.split('-')
    if len(date_sections) != 3:
        raise ValueError('Date should have three sections separated with dashes. The full format should be YYYY-MM-DD')
    try:
        [int(x) for x in date_sections]
    except ValueError:
        raise ValueError('All sections in the date must be numbers')
    year, month, day = date_sections
    if len(year) != 4:
        raise ValueError('Year should be four digits, the full format being YYYY-MM-DD')
    if len(month) != 2:
        raise ValueError('Month should be two digits, the full format being YYYY-MM-DD')
    if len(day) != 2:
        raise ValueError('Day should be two digits, the full format being YYYY-MM-DD')


def validate_time(time: str) -> None:
    if not time:
        pass
    time_sections = time.split(':')
    try:
        [int(x) for x in time_sections]
    except ValueError:
        raise ValueError('All sections of time must be numbers')
    if len(time_sections) > 3:
        raise ValueError('There can be no more than three time sections')
    if len(time_sections) == 3:
        hours, minutes, seconds = [int(x) for x in time_sections]
        if hours < 0 or hours > 23:
            raise ValueError('Hours must be between 0 and 24')
        if minutes < 0 or minutes > 59:
            raise ValueError('Minutes must be between 0 and 59')
        if seconds < 0 or seconds > 59:
            raise ValueError('Seconds must be between 0 and 59')
    if len(time_sections) == 2:
        hours, minutes = [int(x) for x in time_sections]
        if hours < 0 or hours > 23:
            raise ValueError('Hours must be between 0 and 24')
        if minutes < 0 or minutes > 59:
            raise ValueError('Minutes must be between 0 and 59')
    if len(time_sections) == 1:
        hours = int(time_sections[0])
        if hours < 0 or hours > 23:
            raise ValueError('Hours must be between 0 and 24')


def parse_iso8601(timestamp: str) -> datetime.datetime:
    """Parse an ISO-8601 formatted time stamp."""
    if 'T' in timestamp:
        date, time = timestamp.split('T')
    else:
        date, time = timestamp, '00:00:00'
    try:
        validate_time(time)
        validate_date(date)
    except ValueError as e:
        raise e

    year, month, day = [int(num) for num in date.split('-')]
    if len(time) == 2:
        time += ':00:00'
    elif len(time) == 5:
        time += ':00'
    hour, minute, second = [int(num) for num in time.split(':')]
    return datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
