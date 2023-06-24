from django.shortcuts import render, redirect

from .models import Photo
from .forms import PhotoCreateForm, PhotoEditForm


def photo_add(request):
    # начин без `if` проверка
    # form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


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
