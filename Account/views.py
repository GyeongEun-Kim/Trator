from Account.decorators import account_ownership_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, UpdateForm

from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView

has_ownership = [account_ownership_required, login_required]


def index(request):
    return render(request, 'Account/index.html')


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
        return redirect("Account:login")
    else:
        form = AuthenticationForm()
        return render(request, "Account/login.html", {"form": form})


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
        return render(request, 'Account/signup.html', {"form": form})


@method_decorator(has_ownership, 'get')
class AccountDetailView(DetailView):
    model = CustomUser
    context_object_name = 'target_user'
    template_name = 'Account/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = CustomUser
    context_object_name = 'target_user'
    form_class = UpdateForm
    success_url = reverse_lazy('Account:index')
    template_name = 'Account/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = CustomUser
    context_object_name = 'target_user'
    success_url = reverse_lazy('Account:login')
    template_name = 'Account/delete.html'
