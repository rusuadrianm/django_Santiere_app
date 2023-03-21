from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Select

from diriginti.models import Diriginte


class DiriginteForm(forms.ModelForm):
    class Meta:
        model = Diriginte
        fields = ['nume', 'prenume', 'AOL', 'email', 'marca', 'activ']
        widgets = {
            'nume': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'prenume': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'AOL': Select(attrs={'class': 'form-control', 'placeholder': 'Please select AOL'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'marca': NumberInput(attrs={'class': 'form-select', 'placeholder': 'please enter your personal number (marca)'}),
        }


class DiriginteUpdateForm(forms.ModelForm):
    class Meta:
        model = Diriginte
        fields = ['nume', 'prenume', 'AOL', 'email', 'marca']

        widgets = {
            'nume': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'prenume': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'AOL': Select(attrs={'class': 'form-control', 'placeholder': 'Please select AOL'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'marca': NumberInput(
                attrs={'class': 'form-select', 'placeholder': 'please enter your personal number (marca)'}),
        }

