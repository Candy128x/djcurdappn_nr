from django.urls import path
from . import views
# from . import static_content_views as scv

urlpatterns = [
    # path('index', scv.index, name='index'),
    path('index', views.index, name='index'),
    path('discount', views.discount, name='discount'),
]
