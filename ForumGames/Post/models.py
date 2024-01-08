from django.db import models
from django.contrib.auth.models import User
from Videogame.models import PossVideogames
from Computer.models import ComponentsComputer
# Create your models here.
class Post(models.Model):
    P_ID_num = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=10)
    Description = models.CharField(max_length=500)
    FPS_ex = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None )
    videogames_id = models.ForeignKey(PossVideogames,on_delete=models.PROTECT, blank=True, null=True)
    computer_id = models.ForeignKey(ComponentsComputer, on_delete=models.PROTECT, null=True)

class RepPost(models.Model):
    R_ID_num = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=10)
    Description = models.CharField(max_length=30)
    Data = models.DateField()
    Post_id = models.ForeignKey(Post, on_delete=models.PROTECT, blank=True, null=True, default=None)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, default=None)
    onlyThatReportOnThatPost = models.CharField(max_length=1000, unique=True) #Somma tra Post_id e User_id



class ComPost(models.Model):
    C_ID_num = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=300)
    Post_id = models.ForeignKey(Post, on_delete=models.PROTECT, blank=True, null=True, default=None)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, default=None)