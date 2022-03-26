from django.shortcuts import render
from django.http import HttpResponse
from .models import Samochody

def wszystkie (request):
    wszystkie = Samochody.objects.all()
    return render(request, 'samochody.html', {'samochody': wszystkie})

def pierwszy (request):
    return render(request, 'BMW.html')

def drugi (request):
    return render(request, 'mercedes.html')

