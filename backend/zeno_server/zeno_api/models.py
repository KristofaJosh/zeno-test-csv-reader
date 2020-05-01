from django.db import models


# Create your models here.
class ZenoCsv(models.Model):
    idd = models.CharField(max_length=50, blank=True)
    timestamp = models.CharField(max_length=200, null=True, blank=False, default='')
    temperature = models.CharField(max_length=200, default='', blank=True)
    duration = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.idd


class ZenoUpload(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
