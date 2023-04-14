from rest_framework.serializers import ModelSerializer

from apps.management.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'starts_at']
