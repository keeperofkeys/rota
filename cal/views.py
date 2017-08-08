import datetime
import calendar
#from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cal.models import TimeChunk


ONE_DAY = datetime.timedelta(days=1)
ONE_SECOND = datetime.timedelta(seconds=1)

class Day:
    def __init__(self, day, month, year):
        self.date, self.month, self.year = day, month, year
        self.start = datetime.datetime(year=year, month=month, day=day)
        self.end = self.start + ONE_DAY - ONE_SECOND

    def chunks(self):
        return TimeChunk.objects.filter(
            (Q(start_time__gte=self.start) & Q(start_time__lte=self.end))
            | (Q(end_time__gte=self.start) & Q(end_time__lte=self.end))
            | (Q(start_time__lte=self.start) & Q(end_time__gte=self.end))
        )

@login_required(login_url='/login/')
def month_view(request, month, year):
    year = int(year)
    month = int(month)
    start = datetime.datetime(year=year, month=month, day=1)
    start_day, no_of_days = calendar.monthrange(year, month)
    prevmonth = (month - 1, year) if month > 1 else (12, year - 1)
    nextmonth = (month + 1, year) if month < 12 else (1, year + 1)

    days = [None for i in range(start_day)]

    for d in range(1, no_of_days + 1):
        day = Day(d, month, year)
        days.append(day)

    while len(days) % 7:
        days.append(None)

    return render(request, 'calendar.html', {
        'days': days,
        'month': month,
        'year': year,
        'monthname': start.strftime("%B"),
        'prev': prevmonth,
        'next': nextmonth
    })





