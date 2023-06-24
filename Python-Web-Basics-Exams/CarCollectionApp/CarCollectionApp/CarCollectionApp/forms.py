from django import forms

from .models import ProfileModel, CarModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput()
        }


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


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
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
