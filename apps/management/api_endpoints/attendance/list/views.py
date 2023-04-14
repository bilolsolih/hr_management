from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from apps.management.api_endpoints.attendance.list.serializers import AttendanceSerializer
from apps.management.models import Attendance


class AttendanceList(generics.GenericAPIView):
    http_method_names = ['get']

    def get(self, request, record_pk=None, user_pk=None):
        if record_pk and user_pk:
            raise ValueError('Provide the id of either the records or the user the records belongs to')
        if user_pk:
            queryset = Attendance.objects.filter(employee__pk=user_pk)
        elif record_pk:
            queryset = get_object_or_404(Attendance, pk=record_pk)
            response = AttendanceSerializer(queryset, many=False)
            return Response(response.data)
        else:
            queryset = Attendance.objects.all()
        response = AttendanceSerializer(queryset, many=True)
        return Response(response.data)
