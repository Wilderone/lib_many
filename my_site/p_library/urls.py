from django.contrib import admin
from django.urls import path
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many

app_name = 'p_library'
urlpatterns = [
    path('', AuthorList.as_view(), name='author_list'),
    path('create', AuthorEdit.as_view(), name='author_create'),
    path('create_many', author_create_many, name='author_create_many'),
    path('create_manyes', books_authors_create_many,
         name='book_author_create_many')
]
