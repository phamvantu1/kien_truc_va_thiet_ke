from django.urls import path
from .views import get_books,  update_book, delete_book, create_book

urlpatterns = [
    path('books/', get_books, name='get_books'),
    # path('books/add/', add_book, name='add_book'),
    path('update-book/<str:pk>/', update_book, name='update_book'),
    path('delete-book/<str:pk>/', delete_book, name='delete_book'),

    path('creat_books/', create_book, name='create_book'),
]