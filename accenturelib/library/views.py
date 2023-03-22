from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, '/admin/library/change_form.html', {'books': books})
