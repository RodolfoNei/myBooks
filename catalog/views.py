from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.models import Book, Author, Genre

def index(request):
    """View function para a home page do site."""

    # Gerar a contagem do número de livros cadastrados
    num_books = Book.objects.all().count()

    # Gerar a contagem de livros segundo cada status
    num_want = Book.objects.filter(status__exact='w').count()
    num_already = Book.objects.filter(status__exact='a').count()
    num_now = Book.objects.filter(status__exact='r').count()

    # Gerar a contagem de autores cadastrados
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_want': num_want,
        'num_already': num_already,
        'num_now': num_now,
        'num_authors': num_authors,
    }

    # Renderizar o template HTML index.html com os dados da var context
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'year', 'genre', 'status']

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'year', 'genre', 'status']

class BookDelete(DeleteView):
     model = Book
     success_url = reverse_lazy('books')

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class AuthorDelete(DeleteView):
     model = Author
     success_url = reverse_lazy('authors')

class GenreCreate(CreateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('index')