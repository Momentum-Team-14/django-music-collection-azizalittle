from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_albums, name='list_albums'),
    path('albums/new', views.create_album, name='create_album'),
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),
    path('albums/<int:pk>/edit/', views.edit_album, name='edit_album'),
    path('albums/<int:pk>/delete/', views.confirm_delete, name='confirm_delete'),
]