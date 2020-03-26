from django.db import models


# Create your models here.

class Earth(models.Model):
    cases = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    updated = models.DateTimeField()


class CountryInfo(models.Model):
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)
    iso3 = models.CharField(max_length=3, null=True)
    iso2 = models.CharField(max_length=2, null=True)
    flag = models.CharField(max_length=256, null=True)


class Country(Earth):
    countryInfo = models.OneToOneField(CountryInfo, on_delete=models.CASCADE)
    casesToday = models.IntegerField()
    deathsToday = models.IntegerField()
    active = models.IntegerField()
    critical = models.IntegerField()
    casesPerMillion = models.IntegerField()
    deathsPerMillion = models.IntegerField()
