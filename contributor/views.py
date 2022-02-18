from django.http.response import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, "contributor/index.html")
