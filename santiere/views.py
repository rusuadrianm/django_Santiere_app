import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from diriginti.models import Diriginte
from santiere.filters import SantierFilter
from santiere.forms import SantierForm1, UpdateSantierFormDispacer, UpdateSantierFormDiriginte1
from santiere.models import Santier


class SantiereCreateView(CreateView):
    template_name = 'santiere/adauga_santier.html'
    model = Santier
    form_class = SantierForm1
    success_url = reverse_lazy('lista_santiere_filtru')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            santier_nou = form.save(commit=False)
            nr_aparitie = Santier.objects.filter(SDA__exact=santier_nou.SDA).count()
            santier_nou.numar_aparitie = nr_aparitie + 1
            santier_nou.save()
        return redirect('lista_santiere_filtru')


# ================ LIST VIEWS =========================

class SantiereListView(ListView):
    template_name = 'santiere/lista_santiere.html'
    model = Santier
    context_object_name = 'all_santiere'


class SantiereListViewFilter(ListView):
    template_name = 'santiere/lista_santiere_filtru.html'
    model = Santier
    context_object_name = 'all_santiere'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'data')
        return ordering

    def get_queryset(self):
        return Santier.objects.all().order_by('data')

    def get_context_data(self, **kwargs):
        data = super(SantiereListViewFilter, self).get_context_data(**kwargs)
        diriginti = Diriginte.objects.all()
        data['get_all_diriginti'] = diriginti

        santiere = Santier.objects.all().order_by('data')
        filters = SantierFilter(self.request.GET, queryset=santiere)
        data['all_santiere'] = filters.qs
        data['filters_form'] = filters.form

        return data

class SantiereListView_Dispacer(ListView):
    template_name = 'santiere/lista_santiere_dispacer.html'
    model = Santier
    context_object_name = 'santiere_fara_diriginte'


class SantiereListView_Diriginte(ListView):
    template_name = 'santiere/lista_santiere_diriginte.html'
    model = Santier
    context_object_name = 'santiere_diriginte'


# ================ UPGRADE VIEWS =========================

class SantiereUpdateViewDispecer(UpdateView):
    template_name = 'santiere/update_santier_dispacer.html'
    model = Santier
    form_class = UpdateSantierFormDispacer
    success_url = reverse_lazy('ls_dispacer')


class SantiereUpdateViewDiriginte1(UpdateView):
    template_name = 'santiere/update_santier_diriginte.html'
    model = Santier
    form_class = UpdateSantierFormDiriginte1
    success_url = reverse_lazy('ls_diriginte')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            entry = form.save(commit=False)
            if entry.poza1 or entry.poza2 or entry.poza3:
                entry.are_poza = "Da"
            if entry.vizita:
                entry.are_vizia = "Da"

            entry.save()

            if entry.status == "in lucru" or entry.status == "amanat":
                next_day = entry.data + datetime.timedelta(days=1)
                if next_day.weekday() == 5:
                    next_day = next_day + datetime.timedelta(days=2)
                elif next_day.weekday() == 6:
                    next_day = next_day + datetime.timedelta(days=1)

                nr_aparitie = entry.numar_aparitie
                new_entry = Santier.objects.create(data=next_day, tip_santier=entry.tip_santier,
                                                   localitate=entry.localitate,
                                                   strada=entry.strada, numar=entry.numar, tip_lucrari='?',
                                                   constructor=entry.constructor, SDA=entry.SDA,
                                                   diriginte=entry.diriginte, numar_aparitie=nr_aparitie+1)
                new_entry.save()
        return redirect('ls_diriginte')


#=========================== DELETE VIEW ==========================
class SantierDeleteDiriginteView(DeleteView):
    template_name = 'santiere/sterge_santier.html'
    model = Santier
    success_url = reverse_lazy('ls_diriginte')


#========================== FILTER =================================

