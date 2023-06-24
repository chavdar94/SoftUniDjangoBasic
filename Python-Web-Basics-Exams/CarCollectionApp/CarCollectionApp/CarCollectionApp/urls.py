from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', views.profile_create, name='profile_create'),
        path('details/', views.profile_details, name='profile_details'),
        path('edit/', views.profile_edit, name='profile_edit'),
        path('delete/', views.profile_delete, name='profile_delete'),
    ])),
    path('car/', include([
        path('create/', views.car_create, name='car_create'),
        path('<int:pk>/details/', views.car_details, name='car_details'),
        path('<int:pk>/edit/', views.car_edit, name='car_edit'),
        path('<int:pk>/delete/', views.car_delete, name='car_delete'),
    ])),
]
