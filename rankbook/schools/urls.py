from django.urls import path
from . import views

app_name = "schools"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:school>", views.school_home, name="school_home")
]