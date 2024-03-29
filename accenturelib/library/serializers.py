from rest_framework import serializers
from .models import Comment, Book

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('book_id', 'rate', 'comment')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'