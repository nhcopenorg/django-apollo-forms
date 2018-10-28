from django.db import models
from django.conf import settings


class Asset(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=200, default='NOINFO')
    project = models.CharField(max_length=200, default='NOINFO')    
    forms = models.ManyToManyField('fobi.FormEntry')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

# Create your models here.
