from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class CostomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    photo = models.ImageField(upload_to='photo/profile/%Y/%m/%d/',default='null')
    about = models.CharField(max_length=255,default='null')


class EditProfile(models.Model):
    user = models.ForeignKey(CostomUser,on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True,blank=True)
    photo = models.ImageField(upload_to='photo/profile/%Y/%m/%d/',default='null')
    about = models.CharField(max_length=255,default='null')

    def __str__(self):
        return self.user.username