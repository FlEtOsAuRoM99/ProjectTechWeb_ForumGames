from django.db import models
from django.contrib.auth.models import User
from Videogame.models import PossVideogames
# Create your models here.
class Post(models.Model):
    P_ID_num = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=10)
    Description = models.CharField(max_length=500)
    FPS_ex = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None )
    videogames_id = models.ForeignKey(PossVideogames, on_delete=models.PROTECT, blank=True, null=True, default=None)