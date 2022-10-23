from unicodedata import name
from wsgiref.handlers import read_environ
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home/index.html')