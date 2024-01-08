from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PossVideogames(models.Model):
    name = models.CharField(primary_key=True, max_length=25)
    Description = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None )

    def __str__(self) -> str:
        return self.name[0:20] 
    