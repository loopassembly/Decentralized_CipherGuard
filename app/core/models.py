from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser,BaseUserManager,\
    PermissionsMixin, User, UserManager

# Create your models here.


class Registration(models.Model):
    
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to='media/images', default='default/default.jpg')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.name
  
    
    
    

    

