from django.http import HttpResponse
from django.shortcuts import render, redirect
from time import ctime


# Create your views here.
def this_time(request):
    time1=str(ctime())
    return HttpResponse(f'текущая время:{time1}')

def aboat_us(request):
    return redirect('https://geeks.kg/aboutUs')

def home(request):
    return HttpResponse('Главная страница, URL для использования:this_time/, aboat_us/')