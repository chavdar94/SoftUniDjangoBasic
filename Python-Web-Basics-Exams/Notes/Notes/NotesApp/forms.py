from django import forms

from NotesApp.models import ProfileModel, NoteModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass


class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['title', 'content', 'image_url']


class NoteEditForm(NoteBaseForm):
    pass


class NoteDeleteForm(NoteBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
