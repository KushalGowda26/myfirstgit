from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def My_First(request):
    return HttpResponse("<h1>Welcome To My Frist Page</h1>")
