from rest_framework import serializers
from .models import Cotation


class CotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotation
        fields = ('id', 'name', 'description', 'price', 'cotation_type', 'is_last', 'parent')