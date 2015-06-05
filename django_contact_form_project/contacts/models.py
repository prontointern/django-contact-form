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

    def __unicode__(self):
        return self.firstname + ' ' + self.lastname
