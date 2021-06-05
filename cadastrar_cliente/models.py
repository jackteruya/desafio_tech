from django.db import models
from cpf_field.models import CPFField

class Customer(models.Model):
    cpf = CPFField()
    email = models.EmailField()

    def __unicode__(self):
        return self.cpf
