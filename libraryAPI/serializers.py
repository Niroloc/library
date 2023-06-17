from rest_framework import serializers
from .models import Book, Reader, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_type', 'date')


class BookSerializer(serializers.ModelSerializer):
    events = EventSerializer(source='book_set', many=True)

    class Meta:
        model = Book
        fields = ('id', 'author', 'name', 'available', 'taken', 'events')


class ReaderSerializer(serializers.ModelSerializer):
    events = EventSerializer(source='reader_set', many=True)

    class Meta:
        model = Reader
        fields = ('id', 'name', 'events')


class PostEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_type', 'date', 'book', 'reader')


class PostBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('author', 'name', 'available')


class PostReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ('name', )
