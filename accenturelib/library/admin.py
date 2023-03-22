from django.contrib import admin
from .models import Book, Autor, Editora, Categoria

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ["livro", "editora"]
    search_fields = ["livro", "editora", "autor"]
    autocomplete_fields = ["autor", "editora", "categoria"]

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['name']

class EditoraAdmin(admin.ModelAdmin):
    search_fields = ['name']

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Categoria, CategoriaAdmin)
