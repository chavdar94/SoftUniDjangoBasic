from django.shortcuts import render, redirect

from .forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from .models import CarModel, ProfileModel


def get_profile():
    try:
        return ProfileModel.objects.first()
    except:
        return None


def get_cars():
    return CarModel.objects.all().order_by('pk')


def get_car(pk):
    return CarModel.objects.filter(pk=pk).get()


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
        'hide_nav': True,
    }

    return render(request, 'base/index.html', context)


def catalogue(request):
    cars = get_cars()
    # profile = get_profile()

    context = {
        # 'profile': profile,
        'cars': cars
    }

    return render(request, 'base/catalogue.html', context)


def profile_create(request):
    # profile = get_profile()

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        # 'profile': profile,
        'form': form,
        'hide_nav': True,
    }

    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    # profile = get_profile()
    cars = get_cars()

    total_price = sum([s.price for s in cars])

    context = {
        # 'profile': profile,
        'total_price': total_price
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
        'form': form,
    }

    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    cars = get_cars()

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        form.save()
        for car in cars:
            car_form = CarDeleteForm(request.POST, instance=car)
            car_form.save()

        return redirect('index')

    context = {
        # 'profile': profile
    }

    return render(request, 'profile/profile-delete.html', context)


def car_create(request):
    # profile = get_profile()

    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        # 'profile': profile,
        'form': form
    }

    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    # profile = get_profile()
    car = get_car(pk)

    context = {
        # 'profile': profile,
        'car': car
    }

    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    # profile = get_profile()
    car = get_car(pk)

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        # 'profile': profile,
        'car': car,
        'form': form,
    }

    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    # profile = get_profile()
    car = get_car(pk)

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        # 'profile': profile,
        'car': car,
        'form': form,
    }

    return render(request, 'car/car-delete.html', context)
