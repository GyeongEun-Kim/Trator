from django.urls import path
from .views import *

app_name = "Account"

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup')
]
