from rest_framework.serializers import ModelSerializer

from apps.management.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
