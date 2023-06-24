from django.urls import path, include

from .views import home_page, catalogue, plant_create, plant_details, plant_edit, plant_delete, profile_create, \
    profile_details, profile_edit, profile_delete

urlpatterns = [
    path('', home_page, name='home_page'),
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', plant_create, name='plant_create'),
    path('details/<int:pk>/', plant_details, name='plant_details'),
    path('edit/<int:pk>/', plant_edit, name='plant_edit'),
    path('delete/<int:pk>/', plant_delete, name='plant_delete'),
    path('profile/', include([
        path('create/', profile_create, name='profile_create'),
        path('details/', profile_details, name='profile_details'),
        path('edit/', profile_edit, name='profile_edit'),
        path('delete/', profile_delete, name='profile_delete')
    ]))
]
