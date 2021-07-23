from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def list(request):
    return render(request, 'question.html')
