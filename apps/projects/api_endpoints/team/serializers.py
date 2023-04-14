from rest_framework.serializers import ModelSerializer

from apps.projects.models import Team


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_title', 'members', 'is_active']
