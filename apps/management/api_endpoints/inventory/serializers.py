from rest_framework.serializers import ModelSerializer

from apps.management.models import Inventory


class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
