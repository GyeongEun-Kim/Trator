from django.shortcuts import render
from django.shortcuts import redirect
from .models import Guide
from django.utils import timezone

def show_all_list (request) :
    lists = Guide.objects.all()
    return render(request,'list.html',{'guide_list':lists})

def show_detail(request) :
    return detail.html


def new (request) :
   
    if (request.method == 'POST') :
        newGuide = Guide.objects.create(title = request.POST['title'],
                                        content = request.POST['content'],
                                        writer = "나야",
                                        date = timezone.localtime(),
                                        location = request.POST['location'],
                                       # image = request.POST['image'],
                                        price = request.POST['price']
                                    )
    
    
    return render(request,'new.html')

