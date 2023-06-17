import os
from csv import reader
from celery import shared_task
from .models import Book
from .serializers import BookSerializer


class InvalidFile(Exception):
    """Some error occurred while load data from csv file"""
    pass


@shared_task
def load_csv_task(path):
    with open(path) as f:
        csv_reader = reader(f)
        for row in csv_reader:
            if len(row) != 3:
                raise InvalidFile
            author, name, available = row
            available = int(available)
            books = Book.objects.filter(author=author, name=name)
            if books.count() == 0:
                book = Book(author=author, name=name, available=available)
                book.save()
            else:
                available += books[0].available
                books.update(available=available)
    os.remove(path)
