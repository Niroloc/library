from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    available = models.IntegerField()
    taken = models.IntegerField(default=0)


class Reader(models.Model):
    name = models.CharField(max_length=200)


class Event(models.Model):
    EventType = (('taken', 'taken'), ('returned', 'returned'))

    event_type = models.CharField(max_length=8, choices=EventType)
    date = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='book_set')
    reader = models.ForeignKey(Reader, on_delete=models.PROTECT, related_name='reader_set')
