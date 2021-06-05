from cadastrar_cliente.models import Customer
from django.contrib import admin

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'email')
    list_filter = ['email']

admin.site.register(Customer, CustomerAdmin)
