from django.urls import path
from .views import get_users, user_list
from .views import register, register, login, user_profile, update_user, delete_user

urlpatterns = [
    path('get-all-users/', get_users, name='get_users'),
    path('users/', user_list, name='user_list'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', user_profile, name='profile'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
]
