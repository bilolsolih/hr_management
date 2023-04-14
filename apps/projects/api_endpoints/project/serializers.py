from rest_framework.serializers import ModelSerializer

from apps.projects.models import Project, Team


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['members', 'is_active']


class ProjectSerializer(ModelSerializer):
    team = TeamSerializer(many=False)

    class Meta:
        model = Project
        fields = '__all__'
