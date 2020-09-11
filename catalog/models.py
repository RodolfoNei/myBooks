from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    """Model representando um gênero de livro."""
    name = models.CharField(max_length=200, help_text='Insira um gênero de livro (e.g. Ficção Científica)')

    def __str__(self):
        """String para representar o objeto do Model."""
        return self.name

class Book(models.Model):
    """Model representando um livro."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID única desse livro')

    title = models.CharField(max_length=200)

    # Por enquanto considerar que cada livro tenha apenas um autor
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Insira uma sinopse do livro')

    # Por enquanto representando o ano com uma String
    year = models.CharField(max_length=200, null=True, blank=True)

    genre = models.ManyToManyField(Genre, help_text='Selecione um gênero para esse livro')

    READ_STATUS = {
        ('w', 'Want to read'),
        ('a', 'Already read'),
        ('r', 'Reading now')
    }

    status = models.CharField(
        max_length=1,
        choices=READ_STATUS,
        blank=True,
        default='w',
        help_text='Status'
    )

    def __str__(self):
        """String para representar o objeto do Model."""
        return self.title

    def get_absolute_url(self):
        """Retorna a url para acessar os detalhes do livro."""
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):
    """Model representando um autor."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Date of Death', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Retorna a url para acessar uma instância do autor em particular."""
        return reverse('author-detail', args=[str(self.id)])

    def get_delete_url(self):
        """Retorna a url para acessar uma instância do autor em particular."""
        return reverse('author_delete', args=[str(self.id)])

    def __str__(self):
        """String para representar o objeto do Model."""
        return f'{self.last_name}, {self.first_name}'
