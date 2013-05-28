from django.db import models

# Create your models here.
class ReadingType(models.Model):
    name = models.CharField(max_length=1024)
    def __unicode__(self):
        return self.name


class Reading(models.Model):
    title = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024, null=True)
    reading_type = models.ForeignKey(ReadingType)
    def __unicode__(self):
        return self.title

class Note(models.Model):
    context = models.TextField()
    create_date = models.DateTimeField('date created')

