from rest_framework import serializers
from .models import CotationType


class CotationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotationType
        fields = ['id', 'name', 'description', 'user']