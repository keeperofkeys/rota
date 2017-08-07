from django.db import models
from django.contrib.auth.models import User


class TimeChunk(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User)
    text = models.TextField(blank=True)

    def __str__(self):
        if self.text:
            return self.text
        else:
            #return '%s time chunk starting at %t' % self.user.first_name, self.start_time
            return "{} time chunk starting {:%h %d, %Y} at {:%H:%M}".format(self.user.first_name, self.start_time, self.start_time)