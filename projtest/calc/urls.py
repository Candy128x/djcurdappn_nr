from django.urls import path
from . import views

urlpatterns = [
    path('print_msg/', views.print_msg, name='home'),
    path('read_content_from_file/', views.read_content_from_file, name='home'),
]
