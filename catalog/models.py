from django.db import models

class Genre(models.Model):
    """Model representando um gênero de livro"""
    name = models.CharField(max_length=200, help_text='Insira um gênero de livro (e.g. Ficção Científica)')

    def __str__(self):
        """String para representar o objeto do Model"""
        return self.name