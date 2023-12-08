from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ComponentsComputer(models.Model):
    
    Com_ID_num = models.AutoField(
                    primary_key=True
                                  )
    CPU = models.CharField(max_length=300)
    GPU = models.CharField(max_length=300)
    RAM = models.CharField(max_length=300)
    MEM = models.CharField(max_length=300)
    PSU = models.CharField(max_length=300)
    MOBO = models.CharField(max_length=300)
    PC_Photo = models.ImageField(upload_to="uploads/", null=True, blank=True)
    nickname = models.ForeignKey( User, on_delete=models.PROTECT,blank=True,null=True,default=None, related_name="p_computer")
    
    def proprietario(self):
        return self.nickname.username
    
    def __str__(self) -> str:
        return "Computer di " + self.proprietario() + ": \nCPU: " + self.CPU + "\n,GPU: " + self.GPU + "\n,RAM: " + self.RAM + "\n,MEM: " + self.MEM + "\n,PSU: " + self.PSU + "\n,MOBO: " + self.MOBO
    
    def __dir__(self) -> Iterable:
        return [self.CPU, self.GPU, self.RAM, self.PSU, self.MOBO]
    
    class Meta:
        verbose_name_plural = "Computers"

#Potresti aggiungere altri models per gestire le componentistiche