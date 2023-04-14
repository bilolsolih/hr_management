from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.employees.models import Employee
from .serializers import EmployeeSerializer


class EmployeeList(GenericAPIView):
    queryset = Employee.objects.all()
    http_method_names = ['get']

    def get(self, request):
        employees = Employee.objects.all()
        response = EmployeeSerializer(employees, many=True)
        return Response(response.data)
