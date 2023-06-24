from django import forms

from MyPlantApp.models import ProfileModel, PlantModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ('profile_picture',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

        return self.instance


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_readonly_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

        return self.instance

    def __set_readonly_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
