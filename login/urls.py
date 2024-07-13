from django.urls import path
from .views import index, loginuser, registeruser, logoutt

urlpatterns = [
    path('', index, name='mainpage'),
    path('login/', loginuser, name='login'),
    path('register/', registeruser, name='register'),
    path('logout/', logoutt, name='logout'),
]