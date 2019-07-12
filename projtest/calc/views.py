from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def print_msg(request):
    return HttpResponse('<h1>Hello Django Developer</h1>')  # return text


def read_content_from_file(request):
    return render(request, 'home.html')


def read_content_from_file_param(request):
    return render(request, 'home_param.html', {'name': 'Ashish'})


def add_num(request):
    return render(request, 'add_num.html')


def add_num_oprn(request):
    val1 = request.GET["num1"]
    val2 = request.GET["num2"]
    addn = int(val1) + int(val2)
    return render(request, 'add_num.html', {'result': addn})
