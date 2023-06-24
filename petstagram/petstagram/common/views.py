from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy as pyperclip_copy

from petstagram.photos.models import Photo
from .models import Like
from .forms import CommentForm, SearchForm


def home_page(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()
    user = request.user
    user_liked_photos = [like.to_photo_id for like in user.like_set.all()] if user.is_authenticated else []

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            pet_name = search_form.cleaned_data['pet_name']
            all_photos = all_photos.filter(tagged_pets__name__icontains=pet_name).all()

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
        'user_liked_photos': user_liked_photos,
    }

    return render(request, 'common/home-page.html', context)


def like_func(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()
    try:
        liked_obj = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()
    except TypeError:
        liked_obj = None

    if liked_obj:
        liked_obj.delete()
    else:
        if isinstance(request.user, AnonymousUser):
            return redirect('login')

        like = Like(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    pyperclip_copy(request.META['HTTP_HOST'] + resolve_url('photo_details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.filter(pk=photo_id).get()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
