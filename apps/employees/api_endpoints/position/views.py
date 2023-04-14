from rest_framework import generics

from apps.employees.api_endpoints.position.serializers import PositionSerializer
from apps.employees.models import Position
from apps.employees.permissions import IsAdminOrReadOnly


class PositionList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
