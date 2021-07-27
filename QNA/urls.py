from django.urls import path
from .views import *

urlpatterns = [
    path('', question_list, name="qna_list"),
    path('<str:id>', question_detail, name="q_detail"),
    path('new/', question_new, name= "q_new"),
    path('create/', question_create, name = "q_create"),
    path('edit/<str:id>', question_edit, name="q_edit"),
    path('update/<str:id>', question_update, name="q_update"),
    path('delete/<str:id>', question_delete, name = "q_delete")
]