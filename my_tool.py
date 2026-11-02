# my_tool.py
# Author: Christina Vo


class GroomingSchedule:
    """A tool that looks up available pet grooming appointments."""

    def __init__(self, available_times):
        """Store the available appointment times."""
        self.available_times = available_times

    def find_day(self, text):
        """Find a known day mentioned in the message."""
        for day in self.available_times:
            if day in text.lower():
                return day
        return None

    def times_for(self, day):
        """Return available times or None if the day is unknown."""
        if day in self.available_times:
            return self.available_times[day]
        return None
