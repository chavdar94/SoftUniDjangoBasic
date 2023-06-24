from django.shortcuts import render, redirect

from RecipesApp.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from RecipesApp.models import Recipe


def get_all_recipes():
    return Recipe.objects.all()


def get_recipe(pk):
    return Recipe.objects.filter(pk=pk).get()


def home_page(request):
    recipes = get_all_recipes()

    context = {
        'recipes': recipes
    }

    return render(request, 'base/index.html', context)


def recipe_create(request):
    if request.method == "GET":
        form = RecipeCreateForm()
    else:
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'form': form,
    }

    return render(request, 'recipes/create.html', context)


def recipe_edit(request, pk):
    recipe = get_recipe(pk)

    if request.method == "GET":
        form = RecipeEditForm(instance=recipe)
    else:
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'form': form,
        'recipe': recipe
    }

    return render(request, 'recipes/edit.html', context)


def recipe_delete(request, pk):
    recipe = get_recipe(pk)

    if request.method == "GET":
        form = RecipeDeleteForm(instance=recipe)
    else:
        form = RecipeDeleteForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'form': form,
        'recipe': recipe
    }

    return render(request, 'recipes/delete.html', context)


def recipe_details(request, pk):
    recipe = get_recipe(pk)

    context = {
        'recipe': recipe
    }

    return render(request, 'recipes/details.html', context)
