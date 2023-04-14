from rest_framework.serializers import ModelSerializer

from apps.management.models import Attendance


class AttendanceSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['first_name', 'last_name', 'position', 'arrived_at']
