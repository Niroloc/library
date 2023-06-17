import os

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Reader
from .serializers import BookSerializer, ReaderSerializer, PostBookSerializer, PostReaderSerializer, PostEventSerializer
from .tasks import load_csv_task

from csv import reader


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_readers(request):
    readers = Reader.objects.all()
    serializer = ReaderSerializer(readers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_books(request):
    serializer = PostBookSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def post_readers(request):
    serializer = PostReaderSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def post_event(request):
    serializer = PostEventSerializer(data=request.data)
    if serializer.is_valid():
        book = serializer.validated_data['book']
        if serializer.validated_data["event_type"] == 'taken':
            book.taken += 1
            book.available -= 1
        else:
            book.taken -= 1
            book.available += 1
        book.save()
        event = serializer.save()
        event.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def post_load_from_file(request):
    uploaded = request.FILES['file']
    dir = '/files/'
    if not os.path.exists(dir):
        os.makedirs(dir)
    path = dir + uploaded.name
    with open(path, 'wb') as f:
        for chunk in uploaded.chunks():
            f.write(chunk)

    load_csv_task.delay(path)

    return Response()
