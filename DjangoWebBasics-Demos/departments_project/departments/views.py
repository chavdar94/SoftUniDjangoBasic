from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from .models import Person
from .forms import TestForm, ModelTestForm, DeleteForm


def index(request):
    # Взема всички обекти от таблицата person в базата
    users = Person.objects.all()
    context = {
        'users': users,
        'date': timezone.now()
    }

    return render(request, 'index.html', context)


def profile(request, name, pk):
    # Взема определен потребител по първо име (поле в базата)
    user = Person.objects.filter(first_name=name).filter(pk=pk).get()
    # user = get_object_or_404(Person, first_name=ime)

    context = {
        'user': user
    }

    # redirect със get_absolute_url който е в модела Person
    # return redirect(user)

    return render(request, 'profile.html', context)


def test_form(request):
    if request.method == 'GET':
        # Зарежда празна форма
        form = ModelTestForm()
    else:  # if request.method == 'POST':
        # Зарежда форма със полета от зададен модел във Meta класа във forms.py
        form = ModelTestForm(request.POST)
        # проверява дали въведените данни във формата са валидни
        print()
        if form.is_valid():
            # Ако формата не е ModelForm, а е само Form
            # Вземаме висчки нужни полета от формата

            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            # age = form.cleaned_data.get('age')

            # Създаваме нов обект в базата
            # Person.objects.create(first_name=first_name, last_name=last_name, age=age)
            person = form.save(commit=False)
            print(person.first_name, person.last_name, person.age)
            #  person.first_name = test person.last_name = test preson.age = last None

            print(form.cleaned_data)
            '''
            cleaned_date = {
                'first_name': 'test',
                'last_name': 'test last',
                'city': 'Burgas',
                'pets': <QuerySet [<Pet: Pet object (2)>]>,
                'date_of_birth': datetime.date(1212, 12, 12),
                'age': 811
            }
            '''
            date_of_birth = form.cleaned_data['date_of_birth']
            today = timezone.now()
            your_age = today.year - date_of_birth.year
            person.age = your_age

            # person.save()

            # redirect with named url / view
            return redirect('index')

            # redirect with absolute url
            # return redirect(f'127.0.0.1/departments/profile{form.cleaned_data.get("first_name")}')

            # redirect with relative url
            # return redirect(f'profile/{form.cleaned_data.get("first_name")}/')

    # Името на речника не е от значение
    data = {
        'form': form
    }

    return render(request, 'register.html', data)


def person_pets(request):
    persons = Person.objects.filter(first_name='Test').get()
    persons.pets.all()
    # persons_dict = {person: person.pets.all() for person in persons}

    # for person in persons_dict:
    #     print(f'{person.first_name}: {", ".join(pet.name for pet in persons_dict[person])}')

    context = {
        'persons': persons,
        'person_pets': persons_dict
    }

    return render(request, 'pets.html', context)


def edit(request):
    person = Person.objects.filter(pk=1).get()
    if request.method == 'GET':
        form = TestForm(initial=person.__dict__)
    else:
        form = TestForm(request.POST, initial=person.__dict__)
        if form.is_valid():
            data = form.cleaned_data
            p = Person(**data)
            p.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'edit.html', context)


def delete(request, pk):
    person = Person.objects.filter(pk=pk).get()
    form = DeleteForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'person': person,
        'form': form,
    }

    return render(request, 'delete.html', context)
