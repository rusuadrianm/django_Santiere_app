import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from santiere.forms import SantierForm1, UpdateSantierFormDispacer, UpdateSantierFormDiriginte1, SantierFilterForm
from santiere.models import Santier


class SantiereCreateView(CreateView):
    template_name = 'santiere/adauga_santier.html'
    model = Santier
    form_class = SantierForm1
    success_url = reverse_lazy('lista_santiere')


# ================ LIST VIEWS =========================

class SantiereListView(ListView):
    template_name = 'santiere/lista_santiere.html'
    model = Santier
    context_object_name = 'all_santiere'


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
            entry = form.save()
            if entry.status == "in lucru" or entry.status == "amanat":
                next_day = entry.data + datetime.timedelta(days=1)

                new_entry = Santier.objects.create(data=next_day, tip_santier=entry.tip_santier,
                                                   localitate=entry.localitate,
                                                   strada=entry.strada, numar=entry.numar, tip_lucrari='?',
                                                   constructor=entry.constructor, SDA=entry.SDA,
                                                   diriginte=entry.diriginte)
                new_entry.save()
        return redirect('ls_diriginte')


#=========================== DELETE VIEW ==========================
class SantierDeleteDiriginteView(DeleteView):
    template_name = 'santiere/sterge_santier.html'
    model = Santier
    success_url = reverse_lazy('ls_diriginte')


#========================== FILTER =================================

def filter_santiere(request):
    filter_santier = SantierFilterForm(request.GET, queryset=Santier.objects.all())
    context = { 'form': filter_santier.form,
                'santiere': filter_santier.qs
                }
    return render(request, 'santiere/lista_filtrata.html', context)

#comit 3