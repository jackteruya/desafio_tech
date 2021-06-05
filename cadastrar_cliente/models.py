from django.db import models

class Customer(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()

