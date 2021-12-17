from rest_framework.serializers import ModelSerializer
from .models import Counterparties


class CounterpartiesSerializer(ModelSerializer):
    class Meta:
        model = Counterparties
        fields = '__all__'
