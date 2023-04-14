from django.urls import path
from .api_endpoints.event import views as event_views
from .api_endpoints.attendance import views as attendance_views

app_name = 'management'

urlpatterns = [
    path('attendances/', attendance_views.AttendanceList.as_view(), name='attendance_list_create'),
    path('attendances/<int:pk>/', attendance_views.AttendanceDetail.as_view(), name='attendance_detail_update_destroy'),
    path('events/', event_views.EventList.as_view(), name='event_list_create'),
    path('events/<int:pk>/', event_views.EventDetail.as_view(), name='event_detail_update_destroy'),
]