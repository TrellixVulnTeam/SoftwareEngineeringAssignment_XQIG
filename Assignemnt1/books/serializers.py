from rest_framework import serializers
from books.models import Book, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Book
        fields = ['id', 'created', 'title', 'authors', 'publisher', 'publicationDate', 'numberOfPages', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
    class Meta:
        model = User
        fields = {'id', 'username', 'books'}