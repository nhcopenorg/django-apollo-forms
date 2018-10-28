from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.utils.translation import ugettext
from django.shortcuts import render_to_response, render
from django.contrib.messages.views import SuccessMessageMixin


class SignUpView(SuccessMessageMixin, generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
    # TODO
    # separo el mensaje en dos variable como ejemplo de como pasar un valor dinamico al mensaje
    valor = ' created successfully'
    success_message = f'User {valor}.'

    def get_success_message(self, cleaned_data):
        #  cleaned_data is the cleaned data from the form which is used for string formatting
        return self.success_message % dict(cleaned_data)
