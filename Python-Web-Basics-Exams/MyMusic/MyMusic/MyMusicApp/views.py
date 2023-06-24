from django.shortcuts import render, redirect

from MyMusicApp.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from MyMusicApp.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def get_albums():
    return Album.objects.all()


def get_album(pk):
    return Album.objects.filter(pk=pk).get()


def home(request):
    profile = get_profile()

    if profile is None:
        if request.method == 'GET':
            form = ProfileCreateForm()
        else:
            form = ProfileCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')

        context = {
            'profile': profile,
            'form': form
        }

        return render(request, 'profiles/home-no-profile.html', context)
    else:
        albums = get_albums()
        context = {
            'profile': profile,
            'albums': albums
        }
        return render(request, 'profiles/home-with-profile.html', context)


def album_add(request):
    profile = get_profile()

    # if request.method == 'GET':
    #     form = AlbumCreateForm()
    # else:
    form = AlbumCreateForm()
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'albums/add-album.html', context)


def album_details(request, pk):
    profile = get_profile()
    album = get_album(pk)

    context = {
        'profile': profile,
        'album': album
    }

    return render(request, 'albums/album-details.html', context)


def album_edit(request, pk):
    profile = get_profile()
    album = get_album(pk)

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'profile': profile,
        'form': form,
        'album': album,
    }

    return render(request, 'albums/edit-album.html', context)


def album_delete(request, pk):
    profile = get_profile()
    album = get_album(pk)

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'profile': profile,
        'album': album,
        'form': form,
    }

    return render(request, 'albums/delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums = get_albums()

    context = {
        'profile': profile,
        'albums_length': len(albums),
    }

    return render(request, 'profiles/profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    albums = get_albums()

    if request.method == 'GET':
        profile.delete()
        albums.delete()
        return redirect('home')

    context = {
        'profile': profile
    }

    return render(request, 'profiles/profile-delete.html', context)
