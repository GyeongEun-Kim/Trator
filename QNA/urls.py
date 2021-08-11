from django.urls import path
from .views import *

urlpatterns = [
    path('', question_list, name="qna_list"),
    path('question/<str:id>', question_detail, name="q_detail"),
    path('question/new/', question_new, name= "q_new"),
    path('question/create/', question_create, name = "q_create"),
    path('question/edit/<str:id>', question_edit, name="q_edit"),
    path('question/update/<str:id>', question_update, name="q_update"),
    path('question/delete/<str:id>', question_delete, name = "q_delete"),
    path('search/', question_search, name="q_search"),
    path('answer/new/<str:id>', answer_new, name="a_new"),
    path('answer/create/<str:id>', answer_create, name="a_create"),
    path('answer/edit/<str:id>', answer_edit, name="a_edit"),
    path('answer/update/<str:id>', answer_update, name="a_update"),
    path('answer/delete/<str:id>', answer_delete, name = "a_delete"),
    path('answer/adopt/<str:id>', answer_adopt, name='a_adopt'),
    path('answer/adopt/not/<str:id>', answer_another, name='a_not_adopted')
]