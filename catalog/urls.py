from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<str:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<str:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<str:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<str:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<str:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<str:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('genre/create/', views.GenreCreate.as_view(), name='genre_create'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('genre/<str:pk>/delete/', views.GenreDelete.as_view(), name='genre_delete')
]
