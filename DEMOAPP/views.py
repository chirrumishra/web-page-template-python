from django.shortcuts import render
from django.http import HttpResponse


def hi(req):
    return render(req, 'DEMOAPP/hi.html')


# Create your views here.
