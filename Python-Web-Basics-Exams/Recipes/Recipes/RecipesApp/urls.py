from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('create/', views.recipe_create, name='recipe_create'),
    path('edit/<int:pk>/', views.recipe_edit, name='recipe_edit'),
    path('delete/<int:pk>/', views.recipe_delete, name='recipe_delete'),
    path('details/<int:pk>/', views.recipe_details, name='recipe_details'),
]
