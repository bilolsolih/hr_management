from rest_framework import generics

from .serializers import AttendanceSerializer
from apps.management.models import Attendance


class AttendanceList(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceDetail(generics.RetrieveAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
