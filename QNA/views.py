from django.shortcuts import render

# Create your views here.

def list(request):
    render(request, 'qna_list.html')

