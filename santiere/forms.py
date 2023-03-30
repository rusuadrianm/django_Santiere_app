import django_filters
from django import forms
from django.forms import DateInput, TextInput, Select, FileInput

from santiere.models import Santier


class SantierForm1(forms.ModelForm):
    class Meta:
        model = Santier
        fields = ['data', 'tip_santier', 'localitate', 'strada', 'numar', 'tip_lucrari', 'constructor', 'SDA', 'diriginte']

        widgets ={
            'data': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tip_santier': Select(attrs={'class': 'form-control', 'placeholder': 'Alege tip santier'}),
            'localitate': TextInput(attrs={'class': 'form-control', 'placeholder': 'Localiate'}),
            'strada': TextInput(attrs={'class': 'form-control', 'placeholder': 'strada'}),
            'numar': TextInput(attrs={'class': 'form-control', 'placeholder': '--'}),
            'tip_lucrari': TextInput(attrs={'class': 'form-control', 'placeholder': 'detalii lucrari ce se vor executa'}),
            'constructor': TextInput(attrs={'class': 'form-control', 'placeholder': 'Operator economic'}),
            'SDA': TextInput(attrs={'class': 'form-control', 'placeholder': 'cod proiect de tip ##-##-##/0000'}),
        }

    def __init__(self, *args, **kwargs):
        super(SantierForm1, self).__init__(*args, **kwargs)
        self.fields['diriginte'].required = False



### FORMULAR PENTRU UPDATE SANTIER - Dispacer- ###
class UpdateSantierFormDispacer(forms.ModelForm):
    class Meta:
        model = Santier
        fields = ['data', 'tip_santier', 'localitate', 'strada', 'numar', 'tip_lucrari', 'constructor', 'SDA',
                  'diriginte']

        widgets = {
            'data': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tip_santier': Select(attrs={'class': 'form-control', 'placeholder': 'Alege tip santier'}),
            'localitate': TextInput(attrs={'class': 'form-control', 'placeholder': 'Localiate'}),
            'strada': TextInput(attrs={'class': 'form-control', 'placeholder': 'strada'}),
            'numar': TextInput(attrs={'class': 'form-control', 'placeholder': '--'}),
            'tip_lucrari': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'detalii lucrari ce se vor executa'}),
            'constructor': TextInput(attrs={'class': 'form-control', 'placeholder': 'Operator economic'}),
            'SDA': TextInput(attrs={'class': 'form-control', 'placeholder': 'cod proiect de tip ##-##-##/0000'}),
            'Diriginte': Select(attrs={'class': 'form-control'})
        }


class UpdateSantierFormDiriginte1(forms.ModelForm):
    class Meta:
        model = Santier
        fields = ['status', 'observatie', 'poza1', 'poza2', 'poza3', 'document', 'vizita']

        widgets = {

            'status': Select(attrs={'class': 'form-control'}),
            'observatie': TextInput(attrs={'class': 'form-control', 'placeholder': 'Comentarii...', 'rows': 3}),
            'poza1': FileInput(attrs={'class': 'form-control'}),
            'poza2': FileInput(attrs={'class': 'form-control'}),
            'poza3': FileInput(attrs={'class': 'form-control'}),
            'document': FileInput(attrs={'class': 'form-control'}),
            'vizita': FileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(UpdateSantierFormDiriginte1, self).__init__(*args, **kwargs)
        self.fields['observatie'].required = False
        self.fields['poza1'].required = False
        self.fields['poza2'].required = False
        self.fields['poza3'].required = False
        self.fields['document'].required = False
        self.fields['vizita'].required = False






