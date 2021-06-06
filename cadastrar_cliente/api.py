from rest_framework import viewsets

from cadastrar_cliente.models import Customer
from cadastrar_cliente.serializers import CustomerSerializers

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
