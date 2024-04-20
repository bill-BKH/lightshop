from django.urls import path
from . import views

app_name='user_panel'
urlpatterns = [
    path('carts',views.carts),
    path('details/<int:id>',views.detail , name="detail"),
    path('',views.user_profile),
    path('addresses/',views.addresses,name='address')
]