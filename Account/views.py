from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from Account.models import HelloWorld

# Create your views here.


def index(request):
    return render(request, 'account/index.html')


def signup(request):
    if request.method == 'POST':
        # temp = request.POST.get('email_input')
        # new_hello_world = HelloWorld()
        # new_hello_world.text = temp
        # new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        # return render(request, 'account/signup.html', context={'hello_world_output': new_hello_world})
        return HttpResponseRedirect(reverse('Account:index'))
    # hello_world_list = HelloWorld.objects.all()
    # return render(request, 'account/signup.html', context={'text': hello_world_list})
    return render(request, 'account/signup.html', context={'hello_world_list': hello_world_list})
