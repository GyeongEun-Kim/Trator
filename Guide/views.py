from django.http import request
from django.shortcuts import get_list_or_404, render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Guide
from django.utils import timezone
from django.contrib import auth

def guide_list (request) :
    lists = Guide.objects.all()
    return render(request,'guide_list.html',{'guide_list':lists})

def guide_detail(request,id) :
    guide_detail = get_object_or_404(Guide,pk=id)
    return render (request,'guide_detail.html',{'guide_detail':guide_detail})


def guide_new (request) :
   
    if (request.method == 'POST') :
        newGuide = Guide.objects.create(title = request.POST['title'],
                                        content = request.POST['content'],
                                        writer = request.user.username,
                                        date = timezone.localtime(),
                                        location = request.POST['location'],
                                        price = request.POST['price']
                                    )
        if (request.FILES['image'] is not None) :
            newGuide.image = request.FILES['image']
            newGuide.save()
        return guide_list(request)
    
    if (request.method == 'GET') :
        return render(request,'guide_new.html')

def guide_update (request, id) :
    if (request.method == 'GET') :
        update_guide = get_object_or_404(Guide,pk=id)
        return render (request,'guide_update.html',{'guide_update':update_guide})

    elif (request.method == 'POST') :
        update_guide = Guide.objects.get(pk=id)
        update_guide.title= request.POST['title']
        update_guide.content= request.POST['content']
        update_guide.location= request.POST['location']
        update_guide.price= request.POST['price']
        update_guide.image= request.FILES['image']
        update_guide.save() 
        
        return guide_list(request)

def guide_delete (request, id) :
    if (request.method == 'GET') :
        guide = get_object_or_404(Guide,pk=id) 
        guide.delete()
        return guide_list(request)

def guide_search_by_location (request) :
    location = request.GET['location']
    locations = get_list_or_404(Guide,location=location)
    return render (request, 'guide_search',{'search_list':locations},location)

