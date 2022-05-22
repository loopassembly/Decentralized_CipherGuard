from django.db import models

# Create your models here.
class createmp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=100)
    recovery_pin=models.IntegerField(default=0 ,null=False)
    

    def __str__(self):
        return self.name