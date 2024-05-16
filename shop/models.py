from django.db import models

# Create your models here.
class MainSlider(models.Model):
    picture=models.ImageField(upload_to='Mainsliders')