from django.conf.urls import url
from .views import login

urlpatterns = [
    url('login/' , login),
]