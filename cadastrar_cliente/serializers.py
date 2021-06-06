from rest_framework import serializers

from cadastrar_cliente.models import Customer

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "cpf",
            "email",
        ]