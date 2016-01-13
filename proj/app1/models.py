from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

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


##
# New model for inline formset
#

class Reduction(models.Model):
    '''
    '''
    title = models.CharField(max_length=256,)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app1:reduction_update', args=[str(self.id)])

class Entry(models.Model):
    '''
    '''
    sample_run = models.CharField(max_length=256)
    sample_transmission_run = models.CharField(max_length=256, )
    background_run = models.CharField(max_length=256,)
    background_transmission_run = models.CharField(max_length=256, )
    transmission_run = models.CharField(max_length=256, )
    description = models.CharField(max_length=256,)
    # We can not have ForeignKey for abstract models. It has to be here!!
    reduction = models.ForeignKey(Reduction,
                                      on_delete=models.CASCADE,
                                      related_name="entry",
                                      related_query_name="entry",)
    class Meta:
        ordering = ["id"]
        verbose_name_plural = _("Entries")

    def __unicode__(self):
        return self.description
