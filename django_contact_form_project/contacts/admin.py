from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'firstname',
        'lastname',
        'ip',
        'lat',
        'lng',
    )


admin.site.register(Contact, ContactAdmin)
