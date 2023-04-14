from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.employees.models import Employee
from .serializers import EmployeeSerializer


class EmployeeRetrieve(GenericAPIView):
    queryset = Employee.objects.all()
    http_method_names = ['get']

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        response = EmployeeSerializer(employee, many=False)
        return Response(response.data)
