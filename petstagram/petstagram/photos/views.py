from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import get_user_model

from .models import Photo
from .forms import PhotoCreateForm, PhotoEditForm

UserModel = get_user_model()


class PhotoCreateView(views.CreateView):
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home_page')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance.user = self.request.user
        return form


def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    photo_is_liked_by_user = likes.filter(user=request.user)

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'photo_is_liked_by_user': photo_is_liked_by_user
    }

    return render(request, 'photos/photo-details-page.html', context)


def photo_edit(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo_details', pk=pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete(request, pk):
    photo = Photo.objects.filter(pk=pk)
    photo.delete()
    return redirect('home_page')
