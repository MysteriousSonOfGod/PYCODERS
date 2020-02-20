from django.db import models

# Create your models here.
class CountryNames(models.Model):
    CountryName = models.CharField(max_length=50)
    Capital = models.CharField(max_length=50)
    Currency = models.CharField(max_length=50)
    Language = models.CharField(max_length=50)


    def __str__(self):
        return self.CountryName