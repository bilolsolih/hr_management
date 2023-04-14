from django.urls import path
from .api_endpoints.event import views as event_views
from .api_endpoints.attendance.list.views import AttendanceList

app_name = 'management'

urlpatterns = [
    path('attendances/', AttendanceList.as_view(), name='attendance_list'),
    path('attendances/<int:record_pk>/', AttendanceList.as_view(), name='attendance_detail'),
    path('attendances/by_user/<int:user_pk>/', AttendanceList.as_view(), name='attendance_list_by_employee'),
    path('events/', event_views.EventList.as_view(), name='event_list_create'),
    path('events/<int:pk>/', event_views.EventDetail.as_view(), name='event_detail_update_destroy'),
]
