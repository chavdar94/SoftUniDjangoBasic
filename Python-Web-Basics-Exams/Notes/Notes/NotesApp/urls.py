from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile/', views.profile_page, name='profile_page'),
    path('delete/', views.profile_delete, name='profile_delete'),
    path('add/', views.note_add, name='note_add'),
    path('edit/<int:pk>/', views.note_edit, name='note_edit'),
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
    path('details/<int:pk>/', views.note_details, name='note_details'),
]
