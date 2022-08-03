from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def inventoryHome(request):
    html = "<h1> Hello world</h1>"
    return HttpResponse(html)
