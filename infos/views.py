from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader


def contact(request):
    return render (
        request=request,
        template_name='infos/contact.html', 
        context = {'nbar': 'contact'})

def about(request):
    return render (
        request=request,
        template_name='infos/about.html', 
        context = {'nbar': 'about'})

def home(request):
    return render (
        request=request,
        template_name='infos/home.html', 
        context = {'nbar': 'home'})