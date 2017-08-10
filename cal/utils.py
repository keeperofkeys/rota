import datetime

from django.db.models import Q

from cal.models import TimeChunk


ONE_DAY = datetime.timedelta(days=1)
ONE_SECOND = datetime.timedelta(seconds=1)


def pertinent_chunks(start, end):
    return TimeChunk.objects.filter(
        (Q(start_time__gte=start) & Q(start_time__lte=end))  # start falls within period
        | (Q(end_time__gte=start) & Q(end_time__lte=end))  # end falls within period
        | (Q(start_time__lte=start) & Q(end_time__gte=end))  # chunk entirely encloses period
    )


class Day:
    def __init__(self, day, month, year):
        self.date, self.month, self.year = day, month, year
        self.start = datetime.datetime(year=year, month=month, day=day)
        self.end = self.start + ONE_DAY - ONE_SECOND

    def chunks(self):
        return pertinent_chunks(self.start, self.end)