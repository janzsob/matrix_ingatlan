from django.urls import path
from. import views


urlpatterns = [
    path("", views.home, name="homepage"),
    path("ingatlanok/", views.ingatlanok, name="ingatlanok"),
    path("szolgaltatasok/", views.szolgaltatasok, name="szolgaltatasok"),
]
