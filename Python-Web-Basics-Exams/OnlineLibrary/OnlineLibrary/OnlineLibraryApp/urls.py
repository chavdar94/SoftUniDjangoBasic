from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('add/', views.book_add, name='book_add'),
    path('edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('details/<int:pk>/', views.book_details, name='book_details'),
    path('delete/<int:pk>', views.book_delete, name='book_delete'),
    path('profile/', include([
        path('', views.profile_details, name='profile_details'),
        path('edit/', views.profile_edit, name='profile_edit'),
        path('delete/', views.profile_delete, name='profile_delete'),
    ])),
]
