from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView


def index(request):
    return render(request, 'account/index.html')


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request=request, username=username, password=password)
            if user is not None:
                login(request, user)
        return redirect("Account:index")
    else:
        form = AuthenticationForm()
        return render(request, "Account/login_view.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("Account:index")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("Account:index")
    else:
        form = RegisterForm()
        return render(request, 'Account/signup_view.html', {"form": form})


class AccountDetailView(DetailView):
    model = CustomUser
    context_object_name = 'target_user'
    template_name = 'Account/detail.html'


# def signup(request):
#     # if request.method == 'POST':
#     #     form = UserCreationForm(request.POST)
#     #     if form.is_valid():
#     #         user = form.save()
#     #     return redirect('index')
#     # else:
#     # form = UserCreationForm()
#     return render(request, 'account/signup.html')


# class AccountCreateView(CreateView):
#     model = User
#     form_class = UserCreationForm
#     success_url = reverse_lazy('Account:index')
#     template_name = 'Account/signup.html'


# def signup(request):
#     if request.method == "POST":
#         if request.POST['password1'] == request.POST['password2']:
#             new_user = Account.objects.create(
#                 username=request.POST['username'],
#                 password=request.POST['password1'],
#                 email=request.POST['email'],
#                 # phone_number=request.POST['phone_number']
#             )
#             if new_user.is_valid():
#                 user = new_user.save()
#                 login(request, user)
#             return redirect('index')
#     return render(request, 'account/signup.html')
    #     # temp = request.POST.get('email_input')
    #     # new_hello_world = HelloWorld()
    #     # new_hello_world.text = temp
    #     # new_hello_world.save()

    #     hello_world_list = HelloWorld.objects.all()
    #     # return render(request, 'account/signup.html', context={'hello_world_output': new_hello_world})
    #     return HttpResponseRedirect(reverse('Account:index'))
    # hello_world_list = HelloWorld.objects.all()
    # return render(request, 'account/signup.html', context={'text': hello_world_list})
    # return render(request, 'account/signup.html')

# , context={'hello_world_list': hello_world_list}


# class signup(CreateView):
#     model = User
#     form_class = UserCreationForm
#     success_url = reverse_lazy('account:')
#     template_name = 'Account/signup.html'
