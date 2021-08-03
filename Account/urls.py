from django.urls import path
from django.utils.translation import templatize
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name = "Account"

urlpatterns = [
    path('', index, name='index'),
    # path('signup/', AccountCreateView.as_view(), name='signup'),
    # path('login/', LoginView.as_view(template_name='Account/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', register_view, name='signup'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
