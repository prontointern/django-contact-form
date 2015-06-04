from django.shortcuts import render
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'contact_form.html'
