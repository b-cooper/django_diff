from django.db import models
from django.utils import timezone

class DiffRequest(models.Model):
  value = models.SmallIntegerField() # TODO: limit to 33300
  number = models.PositiveSmallIntegerField(primary_key=True) # TODO: limit to 100
  occurrences = models.PositiveIntegerField(default=0) # could be many occurrences
  last_datetime = models.DateTimeField()

  def save(self, *args, **kwargs):
    ''' On save, update last_datetime and occurrences'''
    self.occurrences = self.occurrences + 1
    self.last_datetime = timezone.now()
    return super(DiffRequest, self).save(*args, **kwargs)