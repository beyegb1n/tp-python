from django.urls import path
from . import views


urlpatterns = [
    path('', views.album_list, name='album_list'), 
    path('<int:album_id>/', views.album_detail, name='album_detail'),
    path('add/', views.add_album, name='add_album'),
]
