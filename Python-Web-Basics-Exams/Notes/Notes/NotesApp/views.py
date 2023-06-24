from django.shortcuts import render, redirect

from NotesApp.forms import ProfileCreateForm, NoteBaseForm, NoteEditForm, NoteDeleteForm
from NotesApp.models import ProfileModel, NoteModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except:
        return None


def get_all_notes():
    return NoteModel.objects.all()


def get_note(pk):
    return NoteModel.objects.filter(pk=pk).get()


def home_page(request):
    profile = get_profile()

    if not profile:
        return home_page_with_no_profile(request)
    return home_page_with_profile(request)


def home_page_with_no_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'form': form
    }

    return render(request, 'profiles/home-no-profile.html', context)


def home_page_with_profile(request):
    profile = get_profile()
    notes = get_all_notes()

    context = {
        'profile': profile,
        'notes': notes
    }

    return render(request, 'profiles/home-with-profile.html', context)


def profile_page(request):
    profile = get_profile()
    notes = get_all_notes()

    context = {
        'profile': profile,
        'notes_len': len(notes),
    }

    return render(request, 'profiles/profile.html', context)


def profile_delete(request):
    profile = get_profile()
    notes = get_all_notes()

    profile.delete()
    notes.delete()

    return redirect('home_page')


def note_add(request):
    profile = get_profile()

    if request.method == 'GET':
        form = NoteBaseForm()
    else:
        form = NoteBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'notes/note-create.html', context)


def note_edit(request, pk):
    profile = get_profile()
    note = get_note(pk)

    if request.method == 'GET':
        form = NoteEditForm(instance=note)
    else:
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'profile': profile,
        'form': form,
        'note': note
    }

    return render(request, 'notes/note-edit.html', context)


def note_delete(request, pk):
    profile = get_profile()
    note = get_note(pk)

    if request.method == 'GET':
        form = NoteDeleteForm(instance=note)
    else:
        # note.delete()
        form = NoteDeleteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'profile': profile,
        'note': note,
        'form': form
    }

    return render(request, 'notes/note-delete.html', context)


def note_details(request, pk):
    profile = get_profile()
    note = get_note(pk)

    context = {
        'profile': profile,
        'note': note
    }

    return render(request, 'notes/note-details.html', context)
