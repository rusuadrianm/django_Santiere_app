import django_filters
from django import forms
from django_filters import DateFilter

from santiere.models import Santier


class SantierFilter(django_filters.FilterSet):

    # loc_santier = [(santier.localitate, santier.localitate.upper()) for santier in Santier.objects.filter(active=True)]
    # lista_localitati = set(loc_santier)
    # constr_santier = [(santier.constructor, santier.constructor.upper()) for santier in Santier.objects.filter(active=True)]
    # lista_constructori = set(constr_santier)

    data_gte = DateFilter(field_name="data", lookup_expr='gte', label="Data de la:",
                               widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}))
    data_lte = DateFilter(field_name="data", lookup_expr='lte', label="Data pana la:",
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    tip_santier = django_filters.CharFilter(lookup_expr='icontains', label="Tip Santier")
    localitate = django_filters.CharFilter(lookup_expr='icontains', label="Localitate")
    constructor = django_filters.CharFilter(lookup_expr='icontains', label="Constructor")
    SDA = django_filters.CharFilter(lookup_expr='icontains', label="SDA")

    class Meta:
        model = Santier
        fields = ['data_gte', 'data_lte', 'tip_santier', 'localitate', 'constructor', 'SDA', 'diriginte']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['tip_santier'].field.widget.attrs.update({'class':'form-control'})
        self.filters['localitate'].field.widget.attrs.update({'class':'form-control'})
        self.filters['constructor'].field.widget.attrs.update({'class':'form-control'})
        self.filters['SDA'].field.widget.attrs.update({'class':'form-control'})
        self.filters['diriginte'].field.widget.attrs.update({'class' : 'form-select'})