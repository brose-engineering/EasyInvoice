from django.urls import path

from . import views

app_name = "customers"
urlpatterns = [
    path("", views.index, name ="index"),
    path("/add", views.add_new, name ="add_new"),
]