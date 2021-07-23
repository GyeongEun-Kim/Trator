from django.shortcuts import render
from .models import Guide

def show_all_list (request) :
    lists = Guide.objects.all()
    return render(request,'guide/list.html',{'guide_lists':lists})

def show_detail(request) :
    return detail.html

def new_view () :
    return 


