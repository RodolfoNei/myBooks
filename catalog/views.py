from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Book, Author, Genre

@login_required
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

class BookListView(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    permission_required = 'catalog.view_book'
    model = Book

class BooksByUserListView(PermissionRequiredMixin, LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    permission_required = 'catalog.view_book'
    model = Book
    template_name ='catalog/book_list_owned_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user).order_by('title')

class BookDetailView(PermissionRequiredMixin, LoginRequiredMixin, generic.DetailView):
    permission_required = 'catalog.view_book'
    model = Book

class BookCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'catalog.add_book'
    model = Book
    fields = ['title', 'author', 'summary', 'year', 'genre', 'status']

class BookUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'catalog.change_book'
    model = Book
    fields = ['title', 'author', 'summary', 'year', 'genre', 'status']

class BookDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'catalog.delete_book'
    model = Book
    success_url = reverse_lazy('books')

class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author

class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author

class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = '__all__'

class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class AuthorDelete(LoginRequiredMixin, DeleteView):
     model = Author
     success_url = reverse_lazy('authors')

class GenreCreate(LoginRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('index')

class GenreListView(LoginRequiredMixin, generic.ListView):
    model = Genre

class GenreDelete(LoginRequiredMixin, DeleteView):
     model = Genre
     success_url = reverse_lazy('index')