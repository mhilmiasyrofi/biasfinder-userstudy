from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting


import requests


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


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
