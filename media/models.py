from distutils.command.upload import upload
from django.db import models

class Img(models.Model):
    image=models.ImageField()
    
    
