from django.shortcuts import render
from django.http import HttpResponse


def hi(req):
    return render(req, 'DEMOAPP/main.html')


# Create your views here.
