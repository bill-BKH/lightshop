from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_profile),
    path('carts',views.carts),
    path('details<int:id>',views.detail , name="detail"),
]
