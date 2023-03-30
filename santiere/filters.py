import django_filters
from django import forms
from django_filters import DateFilter

from santiere.models import Santier


class SantierFilter(django_filters.FilterSet):

    loc_santier = [(santier.localitate, santier.localitate.upper()) for santier in Santier.objects.all()]
    lista_localitati = set(loc_santier)
    constr_santier = [(santier.constructor, santier.constructor.upper()) for santier in Santier.objects.all()]
    lista_constructori = set(constr_santier)

    status_santiere = [(santier.status, santier.status) for santier in Santier.objects.all()]
    lista_statusuri = set(status_santiere)
    lista_tipuri = Santier.tipuri_santier

    lista_poza = (('Da', 'DA'),('Nu', 'NU'))

    data_gte = DateFilter(field_name="data", lookup_expr='gte', label="Data de la:",
                               widget=forms.DateInput(attrs={'class':'form-control form-control-sm', 'type': 'date'}))
    data_lte = DateFilter(field_name="data", lookup_expr='lte', label="Data pana la:",
                                widget=forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'}))

    tip_santier = django_filters.ChoiceFilter(choices=lista_tipuri, label="Tip Santier:")
    localitate = django_filters.ChoiceFilter(choices=lista_localitati, label="Localitate:")
    strada = django_filters.CharFilter(lookup_expr='icontains', label="Strada:")
    numar = django_filters.CharFilter(lookup_expr='icontains', label="Numar:")
    constructor = django_filters.ChoiceFilter(choices=lista_constructori, label="Constructor:")
    SDA = django_filters.CharFilter(lookup_expr='icontains', label="SDA:")

    status = django_filters.ChoiceFilter(choices=lista_statusuri, label="Status:")
    are_poza = django_filters.ChoiceFilter(choices=lista_poza, label="poze incarcate:")
    are_vizita = django_filters.ChoiceFilter(choices=lista_poza, label="vizita santier:")



    class Meta:
        model = Santier
        fields = ['data_gte', 'data_lte', 'tip_santier', 'localitate', 'strada', 'numar', 'constructor',
                  'SDA', 'diriginte', 'status', 'are_poza', 'are_vizita']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['tip_santier'].field.widget.attrs.update({'class':'form-control form-control-sm'})
        self.filters['localitate'].field.widget.attrs.update({'class':'form-control form-control-sm'})
        self.filters['strada'].field.widget.attrs.update({'class':'form-control form-control-sm'})
        self.filters['numar'].field.widget.attrs.update({'class': 'form-control form-select-sm'})
        self.filters['constructor'].field.widget.attrs.update({'class':'form-control form-control-sm'})
        self.filters['SDA'].field.widget.attrs.update({'class':'form-control form-control-sm'})
        self.filters['diriginte'].field.widget.attrs.update({'class' : 'form-control form-select-sm'})
        self.filters['status'].field.widget.attrs.update({'class': 'form-control form-select-sm'})
        self.filters['are_poza'].field.widget.attrs.update({'class': 'form-control form-select-sm', 'style': 'backgroundcolor: #00ffff'})
        self.filters['are_vizita'].field.widget.attrs.update({'class': 'form-control form-select-sm'})
