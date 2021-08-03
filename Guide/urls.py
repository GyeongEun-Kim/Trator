"""Trator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *



urlpatterns = [
    path('',guide_list, name='guide_list'),
    path('detail/<str:id>', guide_detail, name='guide_detail'),
    path('new/',guide_new,name='guide_new'),
    path('delete/<str:id>',guide_delete,name='guide_delete'),
    path('update/<str:id>',guide_update,name='guide_update'),
    path('search/',guide_search_by_location,name='guide_search_by_location'),
    path('kakaopay_index',kakaopay_index,name='kakaopay_index'),
    path('kakaopay_process',kakaopay_process,name='kakaopay_process'),
    path('kakaopay_success',kakaopay_success,name='kakaopay_success'),
    path('kakaopay_fail',kakaopay_fail,name='kakaopay_fail'),
    path('kakaopay_cancel',kakaopay_cancel,name='kakaopay_cancel'),
 
] 

