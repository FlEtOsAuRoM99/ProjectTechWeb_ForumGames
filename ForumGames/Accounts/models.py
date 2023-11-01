from collections.abc import Iterable
from django.db import models

# Create your models here.
class Accounts(models.Model):

    nickname = models.CharField(primary_key=True, max_length=30)
    mail = models.EmailField(unique=True, max_length=50)
    password = models.CharField(max_length=200)
    descr = models.CharField(max_length=500)
  
    def __str__(self) -> str:
        return self.nickname
    
    def __dir__(self) -> Iterable[str]:
        return ["nickname", "mail", "password", "descr"]