from django.db import models
from cpf_field.models import CPFField

class Customer(models.Model):
    cpf = CPFField(max_length=11)
    email = models.EmailField()

    def __unicode__(self):
        return self.cpf
