from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Greeting


import requests
from .utils import get_original_text, get_mutated_text



# Create your views here.
def index(request):

    # return HttpResponse('Hello from Python!')
    if request.method == 'GET':
        id = request.GET.get('id', 1)

    return render(request, "index.html", {"id": id, "original": get_original_text(id), "mutant": get_mutated_text(id)})

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
