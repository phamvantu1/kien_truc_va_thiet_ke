from django.urls import path
from .views import get_users, user_list
from .views import register, register, login, user_profile

urlpatterns = [
    path('get-all-users/', get_users, name='get_users'),
    path('users/', user_list, name='user_list'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', user_profile, name='profile'),
]
