from rest_framework.serializers import ModelSerializer

from apps.employees.models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['position_title', 'first_name', 'last_name', 'salary', 'started_on', 'ends_on', 'is_intern']
