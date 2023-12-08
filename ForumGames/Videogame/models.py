from django.db import models

# Create your models here.
class PossVideogames(models.Model):
    name = models.CharField(primary_key=True, max_length=25)
    Description = models.CharField(max_length=500)
