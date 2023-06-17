from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('get/books/', views.get_books),
    path('get/readers/', views.get_readers),
    path('post/books/', views.post_books),
    path('post/readers/', views.post_readers),
    path('post/event/', views.post_event),
    path('post/load_file/', views.post_load_from_file)
]
