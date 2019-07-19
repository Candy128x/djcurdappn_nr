from django.urls import path, re_path
from . import views

urlpatterns = [
    path('print_msg/', views.print_msg, name='home'),
    path('read_content_from_file/', views.read_content_from_file, name='home'),
    path('read_content_from_file_param/', views.read_content_from_file_param, name='home_param'),
    path('add_num/', views.add_num),
    path('add_num_oprn', views.add_num_oprn),

    # pass parameter in url
    path('subtract/<int:num1>/<int:num2>', views.subtract, name='subtract'),

    # pass parameter in url using regular expression
    re_path(r'^mode/(?P<num1>[0-9])/(?P<num2>[0-9])/$', views.mode, name='mode'),
    # re_path(r'^mode/(?P<num1>[0-9]+)/$', views.mode, name='mode'),

]
