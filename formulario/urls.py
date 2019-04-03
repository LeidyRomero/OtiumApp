from django.conf.urls import url
from . import views

urlpatterns = {
    url('new/' , views.formulario, name = "formulario"),
}