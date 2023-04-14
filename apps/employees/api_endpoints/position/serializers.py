from rest_framework.serializers import ModelSerializer

from apps.employees.models import Position


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
