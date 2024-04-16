from django.urls import path
from . import views
app_name = 'user_panel'
urlpatterns = [
    path('',views.user_profile),
    path('carts',views.carts),
    path('details/<int:id>',views.detail , name="detail"),
]
