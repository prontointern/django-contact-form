from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import Contact


class ContactView(TemplateView):
    template_name = 'contact_form.html'

    def get(self, request):
        header = 'Contact Form'
        form = ContactForm()

        return render(
            request,
            self.template_name,
            {
                'header': header,
                'contact_form': form
            }
        )

    def post(self, request):
        header = 'Contact Form'
        form = ContactForm(data=request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            Contact.objects.create(
                firstname=firstname,
                lastname=lastname
            )

        return render(
            request,
            self.template_name,
            {
                'header': header,
                'contact_form': form
            }
        )
