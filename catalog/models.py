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

    title = models.Charfield(max_length=200)

    # Por enquanto considerar que cada livro tenha apenas um autor
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Insira uma sinopse do livro')

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
        default='w'
        help_text='Status'
    )

    def __str__(self):
        """String para representar o objeto do Model."""
        return self.title

    def get_absolute_url(self):
        """Retorna a url para acessar os detalhes do livro."""
        return reverse('book-detail', args=[str(self.id)])