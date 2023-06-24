from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from .forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, ProfileEditForm
from .models import Plant, Profile


# def index(request):
#     return render(request, 'common/home-page.html')


class IndexView(views.TemplateView):
    template_name = 'common/home-page.html'


# def catalogue(request):
#     return render(request, 'common/catalogue.html')


class CatalogueView(views.ListView):
    model = Plant
    template_name = 'common/catalogue.html'


# def profile_create(request):
#     form = ProfileCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('catalogue')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'profile/create-profile.html', context)


class ProfileCreateView(views.CreateView):
    form_class = ProfileCreateForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('catalogue')


# def profile_details(request):
#     plants = Plant.objects.all()
#     context = {
#         'plants': plants
#     }
#     return render(request, 'profile/profile-details.html', context)


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'
    extra_context = {'plants': Plant.objects.all()}

    def get_object(self, queryset=None):
        return Profile.objects.first().pk


# def profile_edit(request):
#     profile = Profile.objects.first()
#     form = ProfileEditForm(request.POST or None, instance=profile)
#     if form.is_valid():
#         form.save()
#         return redirect('profile-details')
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'profile/edit-profile.html', context)


class ProfileEditView(views.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('profile-details')


# def profile_delete(request):
#     profile = Profile.objects.first()
#     # plants = Plant.objects.all()
#     if request.method == 'POST':
#         profile.delete()
#         # plants.delete()
#         return redirect('index')
#
#     return render(request, 'profile/delete-profile.html')


class ProfileDeleteView(views.DeleteView):
    model = Profile
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('index')

    def get(self, *args, **kwargs):
        self.kwargs['pk'] = Profile.objects.first().pk
        return super().get(*args, **kwargs)

    # def get_object(self, queryset=None):
    #     return Profile.objects.first().pk
    #
    def post(self, *args, **kwargs):
        self.kwargs['pk'] = Profile.objects.first().pk
        return super().post(*args, **kwargs)


# def plant_create(request):
#     profile = Profile.objects.first()
#     form = PlantCreateForm(request.POST or None)
#     if form.is_valid():
#         plant = form.save(commit=False)
#         plant.profile = profile
#         form.save()
#         return redirect('catalogue')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'plants/create-plant.html', context)


class PlantCreateView(views.CreateView):
    form_class = PlantCreateForm
    template_name = 'plants/create-plant.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        profile = Profile.objects.first()
        form.instance.profile = profile
        return super().form_valid(form)


# def plant_details(request, pk):
#     plant = Plant.objects.filter(pk=pk).get()
#     context = {
#         'plant': plant
#         # 'plant': Plant.objects.filter(pk=pk).get()
#     }
#     return render(request, 'plants/plant-details.html', context)


class PlantDetailsView(views.DetailView):
    model = Plant
    template_name = 'plants/plant-details.html'


# def plant_edit(request, pk):
#     plant = Plant.objects.filter(pk=pk).get()
#     form = PlantEditForm(request.POST or None, instance=plant)
#     if form.is_valid():
#         form.save()
#         return redirect('catalogue')
#
#     context = {
#         'form': form,
#         'plant': plant
#     }
#     return render(request, 'plants/edit-plant.html', context)


class PlantEditView(views.UpdateView):
    model = Plant
    form_class = PlantEditForm
    template_name = 'plants/edit-plant.html'
    success_url = reverse_lazy('catalogue')

# def plant_delete(request, pk):
#     plant = Plant.objects.filter(pk=pk).get()
#     form = PlantDeleteForm(request.POST or None, instance=plant)
#     if form.is_valid():
#         form.save()
#         return redirect('catalogue')
#
#     context = {
#         'form': form,
#         'plant': plant
#     }
#     return render(request, 'plants/delete-plant.html', context)


class PlantDeleteView(views.DeleteView, PlantEditView):
    model = Plant
    template_name = 'plants/delete-plant.html'
    success_url = reverse_lazy('catalogue')
    form_class = PlantDeleteForm

    def get_context_data(self, **kwargs):
        context = super(PlantEditView, self).get_context_data(**kwargs)
        return context
