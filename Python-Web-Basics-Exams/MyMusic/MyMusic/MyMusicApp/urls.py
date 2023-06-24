from django.urls import path, include
from . import views

urlpatterns = (
    path('', views.home, name='home'),
    path('album/', include([
        path('add/', views.album_add, name='album_add'),
        path('details/<int:pk>/', views.album_details, name='album_details'),
        path('edit/<int:pk>/', views.album_edit, name='album_edit'),
        path('delete/<int:pk>/', views.album_delete, name='album_delete'),
    ])),
    path('profile/', include([
        path('details/', views.profile_details, name='profile_details'),
        path('delete/', views.profile_delete, name='profile_delete'),
    ])),
)
