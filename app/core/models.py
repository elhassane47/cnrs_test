from django.db import models
from django_countries.fields import CountryField


class Brand(models.Model):

    name = models.CharField(max_length=128)
    founder = models.CharField(max_length=128)
    country = CountryField()

    def __str__(self):
        return self.name


class Tablet(models.Model):

    name = models.CharField(max_length=128)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    storage_size = models.IntegerField(default=0, help_text="Storage size in Go")
    release_year = models.DateField()

    def __str__(self):
        return self.name

