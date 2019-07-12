from django.urls import path
from . import views

urlpatterns = [
    path('print_msg/', views.print_msg, name='home'),
    path('read_content_from_file/', views.read_content_from_file, name='home'),
    path('read_content_from_file_param/', views.read_content_from_file_param, name='home_param'),
    path('add_num/', views.add_num),
    path('add_num_oprn', views.add_num_oprn),
]
