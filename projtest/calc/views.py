from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def print_msg(request):
    return HttpResponse('<h1>Hello Django Developer</h1>')  # return text

def read_content_from_file(request):
    return render(request, 'home.html')
