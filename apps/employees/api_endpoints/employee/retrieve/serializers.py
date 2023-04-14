from rest_framework.serializers import ModelSerializer

from apps.employees.api_endpoints.position.serializers import PositionSerializer
from apps.employees.models import Employee


class EmployeeSerializer(ModelSerializer):
    position = PositionSerializer(many=False, read_only=True)

    class Meta:
        model = Employee
        fields = [
            'position', 'first_name', 'last_name', 'salary',
            'started_on', 'ends_on', 'is_intern', 'teams',
            'attendance_records'
        ]
