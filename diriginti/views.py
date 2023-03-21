from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from diriginti.forms import DiriginteForm, DiriginteUpdateForm
from diriginti.models import Diriginte


class DiriginteCreateView(CreateView):
    template_name = 'diriginti/creaza_diriginte.html'
    model = Diriginte
    form_class = DiriginteForm
    success_url = reverse_lazy('homepage')

class DiriginteListView(ListView):
    template_name = 'diriginti/lista_diriginti.html'
    model = Diriginte
    context_object_name = 'all_diriginti'


class DiriginteUpdateView(UpdateView):
    template_name = 'diriginti/update_diriginte.html'
    model = Diriginte
    form_class = DiriginteUpdateForm
    success_url = reverse_lazy('lista_diriginti')



