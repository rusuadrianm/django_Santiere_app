from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from userextend.forms import UserExtendForm, UserEditProfileForm
from userextend.models import ProfilUser


class UserExtendCreateView(CreateView):
    template_name ="userextend/create_user.html"
    model = User
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_user = form.save(commit=False)
            new_user.username = new_user.email

            new_user.save()

        return redirect('login')


class EditProfileView(CreateView):
    template_name ='userextend/edit_profile.html'
    model = ProfilUser
    form_class = UserEditProfileForm
    success_url = reverse_lazy('homepage')

