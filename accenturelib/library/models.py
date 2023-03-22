from django.db import models

# Create your models here.
class Book(models.Model):
    autor = models.ForeignKey("Autor", on_delete=models.DO_NOTHING)
    editora = models.ForeignKey("Editora", on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey("Categoria", on_delete=models.DO_NOTHING)
    livro = models.CharField(max_length=255)

    list_filter = ('livro', 'editora')

    def __str__(self):
        return self.livro


class Autor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Editora(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Categoria(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
