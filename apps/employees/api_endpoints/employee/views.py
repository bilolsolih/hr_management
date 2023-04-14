from rest_framework import generics

from apps.employees.api_endpoints.employee.serializers import EmployeeSerializer
from apps.employees.models import Employee


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
