from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("home page")


def contacts(request):
    return HttpResponse("contacts page")


def about(request):
    return HttpResponse("about page")

def shops(request):
    return HttpResponse("shops")