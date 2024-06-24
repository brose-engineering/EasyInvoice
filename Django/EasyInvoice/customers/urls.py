from django.urls import path

from . import views

app_name = "customers"
urlpatterns = [
    path("", views.index, name ="index"),
    path("add", views.add_new, name ="add_new"),
    path("edit/<int:customer_id>", views.edit, name="edit"),
    path("delete/<int:customer_id>", views.delete, name="delete")
]