from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
        path('',views.home,name='home'),
        path('<slug:slug>', views.product_detail, name='product_detail'),
        path('cat/<str:category>',views.product_by_cat, name='product_by_cat')

]