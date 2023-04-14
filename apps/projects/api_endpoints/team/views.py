from rest_framework import generics

from apps.projects.api_endpoints.project.serializers import TeamSerializer
from apps.projects.models import Team


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
