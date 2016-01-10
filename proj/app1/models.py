from __future__ import unicode_literals

from django.db import models

class DataManager(models.Manager):
    def create_entry(self, entry, sample, background):
        entry = self.create( entry=entry, sample=sample, background=background)
        return entry

class Data(models.Model):
    entry = models.DecimalField(max_digits=5, decimal_places=0)
    sample = models.CharField(max_length=100)
    background = models.CharField(max_length=100)

    objects = DataManager()

    def __unicode__(self):
        return 'Sample: %s :: Background: %s' % (self.sample, self.background)
