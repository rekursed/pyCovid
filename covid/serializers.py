from rest_framework.serializers import ModelSerializer
from .models import Earth, Country, CountryInfo


class EarthSerializer(ModelSerializer):
    class Meta:
        model = Earth
        fields = ['cases', 'deaths', 'recovered', 'updated']


class CountryInfoSerializer(ModelSerializer):
    class Meta:
        model = CountryInfo
        fields = ['lat', 'long', 'iso3', 'iso2', 'flag']


class CountrySerializer(ModelSerializer):
    countryInfo = CountryInfoSerializer(read_only=True)

    class Meta:
        model = Country
        fields = ['cases', 'casesToday', 'deaths', 'deathsToday',
                  'recovered', 'active', 'critical', 'updated',
                  'casesPerMillion', 'deathsPerMillion']
