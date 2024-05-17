from django.db import models
from account.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class blog(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    created_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="blog")
    main_text = RichTextField(null=True,blank=True)
    slug = models.SlugField()

class blog_comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(blog , on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    text = models.CharField(max_length=512)
    admin_respond = models.CharField(max_length=512, blank=True)
    admin_vrify = models.BooleanField(default=False)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    user_liked = models.ManyToManyField(User ,blank=True, related_name='blog_liked')
    user_dislike = models.ManyToManyField(User ,blank=True, related_name="blog_disliked")

    def has_user_liked(self, user):
        return user in self.user_liked.all()
    def has_user_disliked(self , user):
        return user in self.user_dislike.all()