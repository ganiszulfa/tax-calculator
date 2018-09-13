from rest_framework import serializers
from .models import TaxObject

class TaxObjectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, allow_blank=False)
    tax_code = serializers.IntegerField(required=True)
    amount = serializers.IntegerField(required=True)
    tax_amount = serializers.DecimalField(required=False, max_digits=10, decimal_places=3, default=1)
    total_amount = serializers.DecimalField(required=False, max_digits=10, decimal_places=3, default=1)

    class Meta:
        model = TaxObject
        fields = ('id', 'name', 'tax_code', 'amount', 'tax_amount', 'total_amount')
