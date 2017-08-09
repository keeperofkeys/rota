from django.db import models
from django.contrib.auth.models import User

AVAILABILITY_OPTIONS = (
    (u'unavailable', u'Unavailable'),
    (u'available', u'Available'),
    (u'unsure', u'Unsure'),
)

class TimeChunk(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(auto_now=True)
    availability = models.CharField(max_length=12, choices=AVAILABILITY_OPTIONS)

    def __str__(self):
        if self.text:
            return self.text
        else:
            return "{} time chunk starting {:%h %d, %Y} at {:%H:%M}".format(self.user.first_name, self.start_time, self.start_time)

