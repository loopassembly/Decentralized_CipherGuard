import datetime
from sys import platform
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser,BaseUserManager,\
    PermissionsMixin, User, UserManager
from django.utils import timezone
import django.utils
from django.conf import settings
from django.utils.timezone import activate
activate(settings.TIME_ZONE)
# Create your models here.
datetime.datetime.today()

class Registration(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to='media/images', default='default/default.jpg')
    date_created = models.CharField(max_length=200, null=True,default=timezone.now())
    
    
    def __str__(self):
        return self.name
  
class Userpassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform=models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    decrpt_key = models.CharField(max_length=200)
    date_created = models.DateTimeField( null=True, default=django.utils.timezone.now)
  
    
    def __str__(self):
        return self.platform
    
    
    

    

