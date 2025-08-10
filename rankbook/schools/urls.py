from django.urls import path
from . import views

app_name = "schools"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:school_id>", views.school_home, name="school_home")
]