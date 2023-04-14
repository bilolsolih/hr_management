from rest_framework.serializers import ModelSerializer

from apps.employees.api_endpoints.position.serializers import PositionSerializer
from apps.projects.api_endpoints.team.serializers import TeamSerializer
from apps.employees.models import Employee


class EmployeeSerializer(ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)
    position = PositionSerializer(many=False, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
