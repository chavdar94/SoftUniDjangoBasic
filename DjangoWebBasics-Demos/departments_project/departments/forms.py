from django import forms
from django.core.exceptions import ValidationError

from .models import Person

'''
ModelTestForm:

Форма със модел - използва полета от зададения модел в 
Meta класа, могат да се подадат като списък и в него се 
подават имената на полетата от модела в кавички, 
може и да се вземат всичките с '__all__', 
може и да се изключат полета като начина е 
същия като със списъка, но вместо 'fields' се ползва 'exclude'
'''


class ModelTestForm(forms.ModelForm):
    # Disabled form fields

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    # self.__set_disabeld_fields()

    # def __set_disabeld_fields(self):
    #     for field in self.fields.values():
    #         field.widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['age']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_placeholders()

    def __set_placeholders(self):
        for name, value in self.fields.items():
            placeholder = name.split('_')
            value.widget.attrs['placeholder'] = ' '.join(s.capitalize() for s in placeholder)


'''
TestForm:
Форма без зададен модел - дефинираме полетата като атрибути както във моделите.
'''


class TestForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    city = forms.CharField(max_length=50)


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # widgets = {
        #     'date_of_birth': forms.DateInput(format='%d / %m / %Y'),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
