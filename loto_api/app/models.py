from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Record(models.Model):
    _id = models.IntegerField(null=False, blank=False)
    date = models.CharField(null=False, blank=False, max_length=10)
    recordType = models.CharField(null=False, blank=False, max_length=3)
    values = ArrayField(
                models.CharField(max_length=6, blank=True)
            )
    @classmethod
    def create(cls, _id, date, recordType, values):
        record = cls(_id=_id, date=date, recordType=recordType, values=values)
        return record
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)