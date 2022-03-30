from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.
from .models import Read, Choice

def index(request):
    read_list = Read.objects.all()
    context = {'read_list': read_list}
    return render(request, 'proj/index.html', context)

def read(request):
    read_list = Read.objects.all()
    context = {'read_list': read_list}
    return render(request, 'proj/read.html', context)
