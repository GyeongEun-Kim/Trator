from django.urls import path
from .views import *

urlpatterns = [
    path('', question_list, name="list"),
    path('<str:id>/', question_detail, name="qna_detail"),
    path('new/', question_new, name= "qna_new"),
    path('create/', question_create, name = "qna_create"),
]