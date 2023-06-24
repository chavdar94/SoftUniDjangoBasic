from django.shortcuts import render, redirect

from MyPlantApp.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from MyPlantApp.models import ProfileModel, PlantModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def get_plant(pk):
    plant = PlantModel.objects.filter(pk=pk).get()
    return plant


def home_page(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'base/home-page.html', context)


def catalogue(request):
    profile = get_profile()
    plants = sorted(PlantModel.objects.all(), key=lambda x: x.pk)

    context = {
        'plants': plants,
        'plants_len': len(plants),
        'profile': profile
    }
    return render(request, 'base/catalogue.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    plants = PlantModel.objects.all()

    context = {
        'profile': profile,
        'plants': plants
    }

    return render(request, 'profile/profile-details.html', context)


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
    plants = PlantModel.objects.all()

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        form.save()
        for plant in plants:
            plant_form = PlantDeleteForm(request.POST, instance=plant)
            plant_form.save()

        return redirect('home_page')

    context = {
        'profile': profile
    }

    return render(request, 'profile/delete-profile.html', context)


def plant_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'plants/create-plant.html', context)


def plant_details(request, pk):
    plant = get_plant(pk)
    profile = get_profile()

    context = {
        'plant': plant,
        'profile': profile
    }

    return render(request, 'plants/plant-details.html', context)


def plant_edit(request, pk):
    profile = get_profile()
    plant = get_plant(pk)

    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'plant': plant,
        'form': form
    }
    return render(request, 'plants/edit-plant.html', context)


def plant_delete(request, pk):
    profile = get_profile()
    plant = get_plant(pk)

    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'plant': plant,
        'form': form
    }
    return render(request, 'plants/delete-plant.html', context)
