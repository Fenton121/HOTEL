# Create your models here.
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(u"Building name", max_length=50, null=False,
                            blank=False)

    class Meta:
        verbose_name = u"Building"
        verbose_name_plural = u"Buildings"
        
    def __unicode__(self):
        return u"%s) %s" % (self.id, self.name)

    def get_absolute_url(self):
        return reverse('structure:house_edit', kwargs={'pk': str(self.id)})


class Floor(models.Model):
    number = models.IntegerField(u"Floor no", null=False, blank=False)
    house = models.ForeignKey(House, null=False)

    class Meta:
        verbose_name = u"Floor"
        verbose_name_plural = u"Floors"

    def __unicode__(self):
        return u"%s) floor=%s" % (self.id, self.number)

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_absolute_url(self):
        return reverse('structure:floor_edit',
            kwargs={
                 'pk': str(self.id),
                 'house_id': str(self.house.id)
             }
        )


class Chamber(models.Model):
    description = models.TextField(u"Chamber description", null=True)
    house = models.ForeignKey(House, null=False)
    
    class Meta:
        verbose_name = u"Special chamber"
        verbose_name_plural = u"Special chambers"

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_absolute_url(self):
        return reverse('structure:chamber_edit',
            kwargs={
                 'pk': str(self.id),
                 'house_id': str(self.house.id)
             }
        )


class Room(models.Model):
    beds = models.IntegerField(u"Beds number", null=False, blank=False)
    name = models.CharField(u"Name", max_length=10, null=False, blank=False,
                            default='')
    for_disabled = models.BooleanField(u"For disabled", default=False)
    floor = models.ForeignKey(Floor, null=False)

    def __unicode__(self):
        return u"%s) floor=%s, name=%s beds=%s" %\
            (self.id, self.floor.number, self.name, self.beds)

    class Meta:
        verbose_name = u"Room"
        verbose_name_plural = u"Rooms"

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_absolute_url(self):
        return reverse('structure:room_edit',
            kwargs={
                 'pk': str(self.id),
                 'house_id': str(self.floor.house.id),
                 'floor_id': str(self.floor.id)
             }
        )
