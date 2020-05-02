from django.db import models


# Create your models here.
class ZenoCsv(models.Model):
    idd = models.CharField(max_length=50, blank=True)
    temperature = models.CharField(max_length=200, default='', blank=True)
    duration = models.CharField(max_length=200, default='', blank=True)
    timestamp = models.CharField(max_length=200, null=True, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.idd


class ZenoLogger(models.Model):
    method = models.CharField(max_length=6, default='', null=True)
    timestamp = models.DateTimeField(auto_now=True)
