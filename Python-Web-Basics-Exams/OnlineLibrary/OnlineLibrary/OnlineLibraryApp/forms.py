from django import forms

from OnlineLibraryApp.models import ProfileModel, BookModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL'
                }
            )
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_readonly_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance

    def __set_readonly_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'


class BookBaseModel(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Type',
                }
            ),
        }


class BookAddForm(BookBaseModel):
    pass


class BookEditForm(BookBaseModel):
    pass
