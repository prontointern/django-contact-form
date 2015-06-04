from django.shortcuts import render
from django.views.generic import TemplateView


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
        header = 'Contact Form'
        return render(
            request,
            self.template_name,
            {
                'header': header
            }
        )
