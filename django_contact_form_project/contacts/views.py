from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Contact


class ContactView(TemplateView):
    template_name = 'contact_form.html'

    def get(self, request):
        header = 'Contact Form'

        return render(
            request,
            self.template_name,
            {
                'header': header
            }
        )

    def post(self, request):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        if firstname is not None and lastname is not None:
            Contact.objects.create(
                firstname=firstname,
                lastname=lastname
            )

        return render(
            request,
            self.template_name,
            {}
        )
