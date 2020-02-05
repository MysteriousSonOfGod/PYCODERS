# Create your models here.
from django.db import models

class KKRTEAM(models.Model):
   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   # phonenumber = models.IntegerField()

   def __str__(self):
      return self.name