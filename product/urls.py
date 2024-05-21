from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
        path('',views.home,name='home'),
        path('<slug:slug>', views.product_detail, name='product_detail'),
        path('cat/<str:category>',views.product_by_cat, name='product_by_cat'),
        path('like/',views.like, name='like'),
        path('dislike/',views.dislike, name='dislike'),
        path('reply_to_comment/',views.reply_to_comment,name='reply_to_comment'),
        path('product_create_comment/',views.product_create_comment,name='product_create_comment'),
]