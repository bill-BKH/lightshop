from django.urls import path
from . import views

<<<<<<< HEAD
app_name='user_panel'
urlpatterns = [
    path('carts',views.carts),
    path('details/<int:id>',views.detail , name="detail"),
    path('',views.user_profile),
    path('addresses/',views.addresses,name='address')
]
=======

app_name = 'user_panel'


urlpatterns = [
    path('profile-info/',views.profile_info,name='profile_info'),
    path('profile-edit/',views.profile_edit,name='profile_edit'),
    
]
>>>>>>> a6c731b (commit message)
