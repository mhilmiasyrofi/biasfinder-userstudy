from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Greeting


import requests

id = None


# def index(request):
#     r = requests.get('http://httpbin.org/status/418')
#     print(r.text)
#     return HttpResponse('<pre>' + r.text + '</pre>')

# Create your views here.
def index(request):

    # return HttpResponse('Hello from Python!')
    if request.method == 'GET':
        id = request.GET.get('id', 1)
    return render(request, "index.html", {"id": id})

def next(request): 
    if request.method == 'GET':
        id = int(request.GET.get('id', 1))
        id += 1
    return redirect(f"/?id={id}")

def prev(request): 
    if request.method == 'GET':
        id = int(request.GET.get('id', 1))
        id -= 1
    return redirect(f"/?id={id}")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
