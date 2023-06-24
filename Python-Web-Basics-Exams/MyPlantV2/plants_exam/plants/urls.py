from django.urls import path, include

from . import views

# Function based views urls
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('catalogue/', views.catalogue, name='catalogue'),
#
#     # plant urls
#     path('create/', views.plant_create, name='plant-create'),
#     path('details/<int:pk>/', views.plant_details, name='plant-details'),
#     path('edit/<int:pk>/', views.plant_edit, name='plant-edit'),
#     path('delete/<int:pk>/', views.plant_delete, name='plant-delete'),
#
#     # profile urls
#     path('profile/', include([
#         path('create/', views.profile_create, name='profile-create'),
#         path('details/', views.profile_details, name='profile-details'),
#         path('edit/', views.profile_edit, name='profile-edit'),
#         path('delete/', views.profile_delete, name='profile-delete'),
#     ]))
# ]


# Class based views urls

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),

    # plant urls
    path('create/', views.PlantCreateView.as_view(), name='plant-create'),
    path('details/<int:pk>/', views.PlantDetailsView.as_view(), name='plant-details'),
    path('edit/<int:pk>/', views.PlantEditView.as_view(), name='plant-edit'),
    path('delete/<int:pk>/', views.PlantDeleteView.as_view(), name='plant-delete'),

    # profile urls
    path('profile/', include([
        path('create/', views.ProfileCreateView.as_view(), name='profile-create'),
        path('details/', views.ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
    ]))
]
