from rest_framework import serializers
from .models import *

class MovielistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movielist
        fields = ['id', 'title', 'genre', 'description', 'video', 'created_at', 'updated_at']

class SonglistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songlist
        fields = ['id', 'title', 'artist', 'genre', 'video', 'video', 'created_at', 'updated_at']

class BooklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booklist
        fields = ['id', 'title', 'author', 'genre', 'image', 'created_at', 'updated_at']

