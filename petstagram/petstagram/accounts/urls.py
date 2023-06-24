from django.urls import path, include

from .views import UserCreateView, UserLoginView, UserDetailsView, UserProfileEditView, UserProfileDeleteView, UserLogoutView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='profile_details'),
        path('edit/', UserProfileEditView.as_view(), name='profile_edit'),
        path('delete/', UserProfileDeleteView.as_view(), name='profile_delete'),
    ])),
]
