"""
    File: dates.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: Record the events for the dates and print
        the events for the dates.
"""


def canonicalize_date(date_str):
    """
    Canonicalize a date string to the format YYYY-MM-DD.

    Args:
        date_str (str): A date string in the format yyyy-mm-dd
            or mm/dd/yyyy or MonthName   dd   yyyy.

    Returns:
        str: The date string in the format YYYY-MM-DD.
    """
    months = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
            ]
    date_list = date_str.split()
    if len(date_list) == 1:
        date_list = date_list[0].split("/")
    if len(date_list) == 1:
        date_list = date_list[0].split("-")
    if date_list[0] in months:
        day = date_list[1]
        year = date_list[2]
        month_num = 0
        for i in range(len(months)):
            if date_list[0] == months[i]:
                month_num = i + 1
        return "{:d}-{:d}-{:d}".format(int(year), int(month_num), int(day))
    if 0 < int(date_list[0]) < 13:
        month_num = date_list[0]
        day = date_list[1]
        year = date_list[2]
        return "{:d}-{:d}-{:d}".format(int(year), int(month_num), int(day))
    if len(date_list[0]) == 4:
        year = date_list[0]
        month_num = date_list[1]
        day = date_list[2]
        return "{:d}-{:d}-{:d}".format(int(year), int(month_num), int(day))


class Date:
    """
    This class is used to store the date and the events for the date.

    Attributes:
        date (str): The date in the format YYYY-MM-DD.
        events (list): The list of events for the date.

    Methods:
        add_event(event): Adds the event to the list of events.
    """
    def __init__(self, date, event):
        self.date = date
        self.events = [event]

    def __str__(self):
        return self.date

    def add_event(self, event):
        self.events.append(event)


class DateSet:
    """
    This class is used to store the Date class obj.

    Attributes:
        dates (list): The list of Date class obj.

    Methods:
        add_date(date, event): Adds the Date class object to the list of dates.
        get_events_for_date(date): Returns the list of events for the date.
    """
    def __init__(self):
        self.dates = []

    def add_date(self, date, event):
        for i in range(len(self.dates)):
            if self.dates[i].date == date:
                self.dates[i].add_event(event)
                break
        else:
            self.dates.append(Date(date, event))

    def get_events_for_date(self, date):
        for i in range(len(self.dates)):
            if self.dates[i].date == date:
                return self.dates[i].events
        return None

    def __str__(self):
        return str(self.dates)


def main():
    """
    This function is used to read the input file,
        and store and print the events for the dates.

    Args:
        None

    Returns:
        None

    Pre-conditions:
        The input file must exist.

    Post-conditions:
        The events for the dates are printed.
    """
    filename = str(input())
    lines = open(filename, "r").read().splitlines()
    dateset = DateSet()
    for line in lines:
        if line[0] == "I":
            actions = line.split(":")
            date = actions[0][1:].strip()
            canon_date = canonicalize_date(date)
            event = actions[1].strip()
            if len(actions) > 2:
                event = actions[1] + ":" + actions[2]
            dateset.add_date(canon_date, event)
        elif line[0] == "R":
            date = line[1:].strip()
            canon_date = canonicalize_date(date)
            events_for_date = dateset.get_events_for_date(canon_date)
            if events_for_date is not None:
                for event in sorted(events_for_date):
                    print("{}: {}".format(canon_date, event))
        else:
            print("Error - Illegal operation.")


main()
