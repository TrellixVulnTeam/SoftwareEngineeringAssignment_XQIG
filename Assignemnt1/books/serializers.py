from rest_framework import serializers
from books.models import Book, LANGUAGE_CHOICES, STYLE_CHOICES


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'created', 'title', 'author', 'publisher', 'publicationDate', 'numberOfPages']
