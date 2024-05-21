from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.blogs , name='blog'),
    path('<slug:slug>', views.blog_detail , name='blog-detail'),
    path('like/', views.blog_comment_like , name='like'),
    path('dislike/', views.blog_comment_dislike , name='dislike'),
    path('blog_comment_create/', views.blog_comment_create , name='blog_comment'),
    path('blog_reply/', views.blog_reply , name='blog_reply'),

]