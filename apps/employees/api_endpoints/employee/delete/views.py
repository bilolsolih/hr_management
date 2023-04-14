from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.employees.models import Employee


class EmployeeDelete(GenericAPIView):
    queryset = Employee.objects.all()
    http_method_names = ["delete"]

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_200_OK)

# class EmployeeDelete(DestroyAPIView):
#     permission_classes = [AllowAny]
#     queryset = Employee.objects.all()
