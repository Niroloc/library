from django.contrib import admin
from .models import Book, Reader, Event

admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Event)
