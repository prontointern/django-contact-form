from django.db import models


class Contact(models.Model):
    firstname = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    lastname = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=300
    )

    ip = models.CharField(
        null=True,
        blank=True,
        max_length=300
    )

    lat = models.CharField(
        null=True,
        blank=True,
        max_length=300
    )

    lng = models.CharField(
        null=True,
        blank=True,
        max_length=300
    )

    def __unicode__(self):
        return self.firstname + ' ' + self.lastname
