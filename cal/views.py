import datetime
import calendar
#from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cal.models import TimeChunk
from cal.utils import pertinent_chunks, Day, ONE_SECOND, ONE_DAY


@login_required(login_url='/login/')
def month_view(request, month, year):
    year = int(year)
    month = int(month)
    start_day, no_of_days = calendar.monthrange(year, month)
    prevmonth = (month - 1, year) if month > 1 else (12, year - 1)
    nextmonth = (month + 1, year) if month < 12 else (1, year + 1)
    start = datetime.datetime(year=year, month=month, day=1)
    end = datetime.datetime(year=nextmonth[1], month=nextmonth[0], day=1) - ONE_SECOND
    chunks = pertinent_chunks(start, end)

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
        'next': nextmonth,
        'chunks': chunks
    })





