from django.db import models
from django.utils.text import slugify
from account.models import User
# Create your models here.

# class ProductGallery(models.Model):
    

class ProductCategory(models.Model):
    title = models.CharField(max_length=64)
    url_title = models.CharField(max_length=64,null=True,blank=True)
    parent = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title 


class Brand(models.Model):
    title=models.CharField(max_length=300)
    def __str__(self):
           return self.title 

class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    short_description =models.CharField(max_length=260)
    description = models.TextField(help_text="describe the product here")
    slug = models.SlugField()
    category = models.ManyToManyField(ProductCategory)
    is_active = models.BooleanField()
    is_delete = models.BooleanField(default= False)
    picture = models.ImageField(upload_to="product" ,null= True, blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.title } | {self.price}'
    
class ProductComment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parent = models.ForeignKey('ProductComment', on_delete=models.CASCADE, null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    confirmed_by_admin = models.BooleanField(default=False)
    user_liked = models.ManyToManyField(User , related_name='user_liked')
    user_dislike = models.ManyToManyField(User , related_name="user_disliked")

    def has_user_liked(self, user):
        return user in self.user_liked.all()
    def has_user_disliked(self , user):
        return user in self.user_dislike.all()
    
class ProductVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20)