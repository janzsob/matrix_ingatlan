from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Matrix Ingatlan!")


def home(request):
    return render(request, "webapp/home.html")


def ingatlanok(request):
    return render(request, "webapp/ingatlanok.html")


def szolgaltatasok(request):
    return render(request, "webapp/szolgaltatasok.html")
