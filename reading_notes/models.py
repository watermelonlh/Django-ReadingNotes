import time
from django.db import models

# Create your models here.
class ReadingType(models.Model):
    name = models.CharField(max_length=1024)
    def __unicode__(self):
        return self.name


class Reading(models.Model):
    title = models.CharField(max_length=1024, null=True, blank=True)
    author = models.CharField(max_length=1024, null=True, blank=True)
    reading_type = models.ForeignKey(ReadingType)
    def __unicode__(self):
        return "[" + self.reading_type.name + "]" + self.title

class Note(models.Model):
    reading = models.ForeignKey(Reading)
    context = models.TextField()
    create_date = models.DateTimeField('date created')
    def __unicode__(self):
        return unicode(self.reading) + ":" + self.context
