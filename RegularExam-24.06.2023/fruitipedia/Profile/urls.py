from django.urls import path

from .views import ProfileCreate, ProfileEdit, ProfileDetails, ProfileDelete

urlpatterns = [
    path('create/', ProfileCreate.as_view(), name='profile-create'),
    path('details/', ProfileDetails.as_view(), name='profile-details'),
    path('edit/', ProfileEdit.as_view(), name='profile-edit'),
    path('delete/', ProfileDelete.as_view(), name='profile-delete'),
]
