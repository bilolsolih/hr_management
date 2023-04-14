from rest_framework import generics

from apps.projects.api_endpoints.project.serializers import ProjectSerializer
from apps.projects.models import Project


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
