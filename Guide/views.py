from django.http import request
from django.shortcuts import render
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
    return render (request,'guide_detail.html',{'guide_detail',guide_detail})


def guide_new (request) :
   
    if (request.method == 'POST') :
        newGuide = Guide.objects.create(title = request.POST['title'],
                                        content = request.POST['content'],
                                        writer = request.user,
                                        date = timezone.localtime(),
                                        location = request.POST['location'],
                                       # image = request.POST['image'],
                                        price = request.POST['price']
                                    )
        return guide_list(request)
    
    if (request.method == 'GET') :
        return render(request,'guide_new.html')

def guide_update (request) :
    if (request.method == 'GET') :
        update_guide = Guide.objects.get(id=request.GET['id'])
        if (auth.authenticate(request) == update_guide['writer']) :
            return render (request,'update.html',update_guide)
        else :
            return redirect ('/')

    else :
        return redirect('/')

def guide_delete (request, id) :
    guide = Guide.objects.get(pk=id)
    guide.delete()
    return redirect('/')

