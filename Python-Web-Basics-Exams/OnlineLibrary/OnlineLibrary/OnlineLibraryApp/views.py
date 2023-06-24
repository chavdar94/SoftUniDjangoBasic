from django.shortcuts import render, redirect

from OnlineLibraryApp.forms import ProfileCreateForm, BookAddForm, BookEditForm, ProfileEditForm, ProfileDeleteForm
from OnlineLibraryApp.models import ProfileModel, BookModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except:
        return None


def get_all_books():
    return BookModel.objects.all()


def get_book(pk):
    return BookModel.objects.filter(pk=pk).get()


def home(request):
    profile = get_profile()

    if profile:
        return home_with_user(request)

    return home_without_user(request)


def home_with_user(request):
    profile = get_profile()
    books = get_all_books().order_by('pk')

    context = {
        'profile': profile,
        'books': books
    }

    return render(request, 'profile/home-with-profile.html', context)


def home_without_user(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/home-no-profile.html', context)


def book_add(request):
    profile = get_profile()

    if request.method == 'GET':
        form = BookAddForm()
    else:
        form = BookAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'book/add-book.html', context)


def book_edit(request, pk):
    profile = get_profile()
    book = get_book(pk)

    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'profile': profile,
        'book': book,
        'form': form,
    }
    return render(request, 'book/edit-book.html', context)


def book_details(request, pk):
    profile = get_profile()
    book = get_book(pk)

    context = {
        'profile': profile,
        'book': book,
    }

    return render(request, 'book/book-details.html', context)


def book_delete(request, pk):
    book = get_book(pk)
    book.delete()
    return redirect('home_page')


def profile_details(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'profile/profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    books = get_all_books()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        form.save()
        books.delete()
        return redirect('home_page')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)
