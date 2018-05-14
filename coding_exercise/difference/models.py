from django.db import models
from django.utils import timezone

class DiffRequest(models.Model):
  value = models.IntegerField() # NOTE: will never exceed 25164150
  number = models.PositiveSmallIntegerField(primary_key=True) # NOTE: will never exceed 100
  occurrences = models.PositiveIntegerField(default=0)
  datetime = models.DateTimeField()
  last_datetime = models.DateTimeField()

  def save(self, *args, **kwargs):
    ''' On save, update timestamps and occurrences'''
    self.occurrences = self.occurrences + 1
    self.last_datetime = self.datetime or timezone.now()
    self.datetime = timezone.now()
    return super(DiffRequest, self).save(*args, **kwargs)