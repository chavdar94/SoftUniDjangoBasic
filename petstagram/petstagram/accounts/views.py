from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views

from .forms import UserCreateForm, UserLoginForm, UserEditForm
from ..photos.models import Photo

UserModel = get_user_model()


class UserCreateView(views.CreateView):
    model = UserModel
    form_class = UserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home_page')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class UserDetailsView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        photos = self.object.photo_set.prefetch_related('like_set')

        context['is_owner'] = self.request.user == self.object
        context['photos_count'] = self.object.photo_set.all().count()
        context['pet_count'] = self.object.pet_set.count()
        context['total_likes'] = sum(x.like_set.count() for x in photos)
        context['pets'] = self.object.pet_set.all()
        context['photos'] = photos
        return context


class UserProfileEditView(views.UpdateView):
    model = UserModel
    form_class = UserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


class UserProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home_page')
