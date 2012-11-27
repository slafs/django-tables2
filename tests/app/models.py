# coding: utf-8
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy
from django.utils.translation import ugettext


class Person(models.Model):
    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200, verbose_name='surname')

    occupation = models.ForeignKey(
            'Occupation', related_name='people',
            null=True, verbose_name='occupation')

    trans_test = models.CharField(
            max_length=200, blank=True,
            verbose_name=ugettext("translation test"))

    trans_test_lazy = models.CharField(
            max_length=200, blank=True,
            verbose_name=ugettext_lazy("translation test lazy"))

    safe = models.CharField(
            max_length=200, blank=True, verbose_name=mark_safe("<b>Safe</b>"))

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"

    def __unicode__(self):
        return self.first_name

    @property
    def name(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Occupation(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey('Region', null=True)

    def __unicode__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=200)
    mayor = models.OneToOneField(Person, null=True)

    def __unicode__(self):
        return self.name


# -- haystack -----------------------------------------------------------------


from haystack import site
from haystack.indexes import CharField, SearchIndex

class PersonIndex(SearchIndex):
    first_name = CharField(document=True)

site.register(Person, PersonIndex)
