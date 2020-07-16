from django.shortcuts import render
from django.http import HttpResponse
from .models import Ingatlan


def index(request):
    return HttpResponse("Hello Matrix Ingatlan!")


def home(request):
    return render(request, "webapp/home.html")


def ingatlanok(request):
    properties = Ingatlan.objects.all()
    context = {"properties": properties}
    return render(request, "webapp/ingatlanok.html", context)


def szolgaltatasok(request):
    return render(request, "webapp/szolgaltatasok.html")
