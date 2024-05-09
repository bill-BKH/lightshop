from django.db import models

# Create your models here.
class slider(models.Model):
    first_slider=models.ImageField(null=True,blank=True)
    second_slider=models.ImageField(null=True,blank=True)
    third_slider=models.ImageField(null=True,blank=True)
    fourth_slider=models.ImageField(null=True,blank=True)
    fifth_slider=models.ImageField(null=True,blank=True)
    sixth_slider=models.ImageField(null=True,blank=True)
    seventh_slider=models.ImageField(null=True,blank=True)
    sidebar=models.ImageField(null=True,blank=True)