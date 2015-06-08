from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
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
            url = '/thankyou/?firstname=%s' % firstname
            request.session['lastname'] = request.POST.get('lastname')
            return HttpResponseRedirect(url)

        return render(
            request,
            self.template_name,
            {
                'header': header,
                'contact_form': form
            }
        )


class ThankYouView(TemplateView):
    template_name = 'thank_you.html'

    def get(self, request):
        firstname = request.GET.get('firstname')
        lastname = request.session.get('lastname')

        return render(
            request,
            self.template_name,
            {
                'firstname': firstname,
                'lastname': lastname,
            }
        )
