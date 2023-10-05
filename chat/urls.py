from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("key", views.key, name="key"),
    path("clear", views.clear, name="clear") 
]