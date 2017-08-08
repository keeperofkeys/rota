import datetime
import calendar
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cal.models import TimeChunk


@login_required(login_url='/login/')
def cal(request, month, year):
    year = int(year)
    month = int(month)
    start = datetime.datetime(year=year, month=month, day=1)
    end = datetime.datetime(year=year+month//12, month=(month%12)+1, day=1) - datetime.timedelta(seconds=1)
    chunks = TimeChunk.objects.filter(start_time__gte=start, end_time__lte=end)
    start_day, no_of_days = calendar.monthrange(year, month)
    prevmonth = (month - 1, year) if month > 1 else (12, year - 1)
    nextmonth = (month + 1, year) if month < 12 else (1, year + 1)

    cells = [{'cls': 'blank', 'date': 0} for i in range(start_day + 1)]

    for d in range(1, no_of_days + 1):
        cells.append({
            'cls': 'c-%s' % d,
            'date': d
        })

    while len(cells) % 7:
        cells.append({'cls': 'blank', 'date': 0})

    return render(request, 'calendar.html', {
        'chunks': chunks,
        'cells': cells,
        'month': month,
        'year': year,
        'monthname': start.strftime("%B"),
        'prev': prevmonth,
        'next': nextmonth
    })
