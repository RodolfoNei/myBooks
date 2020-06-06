from django.shortcuts import render
from django.views import generic
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

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
