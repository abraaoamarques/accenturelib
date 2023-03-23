from django.contrib.admin import site
from django.contrib import admin
import adminactions.actions as actions
from .models import Book, Autor, Editora, Categoria, Comment, Rate

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
admin.site.register(Comment)
admin.site.register(Rate)
actions.add_to_site(site)
