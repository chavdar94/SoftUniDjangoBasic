from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Pet
from .forms import PetForm, PetDeleteForm


def pet_add(request):
    if request.method == 'GET':
        form = PetForm()
    else:
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('profile_details', pk=request.user.pk)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context)


@login_required
def pet_delete(request, username, pet_slug):
    pet = get_object_or_404(Pet, slug=pet_slug, user=request.user)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile_details', pk=1)

    form = PetDeleteForm(instance=pet)
    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-delete-page.html', context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()
    user = pet.user
    all_photos = pet.photo_set.all()
    is_owner = request.user.pk == pet.user.pk
    user_liked_photos = [like.to_photo_id for like in user.like_set.all()] if user.is_authenticated else []

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'is_owner': is_owner,
        'user_liked_photos': user_liked_photos,
    }

    return render(request, 'pets/pet-details-page.html', context)


@login_required
def pet_edit(request, username, pet_slug):
    pet = get_object_or_404(Pet, slug=pet_slug, user=request.user)

    if request.method == 'GET':
        form = PetForm(instance=pet)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_details', username, pet_slug)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)
