from django.urls import path

from .api_endpoints.attendance.list.views import AttendanceList
from .api_endpoints.event import views as event_views
from .api_endpoints.inventory.views import InventoryList, InventoryDetail
from .api_endpoints.item.views import ItemDetail, ItemList

app_name = 'management'

urlpatterns = [
    path('attendances/', AttendanceList.as_view(), name='attendance_list'),
    path('attendances/<int:record_pk>/', AttendanceList.as_view(), name='attendance_detail'),
    path('attendances/by_user/<int:user_pk>/', AttendanceList.as_view(), name='attendance_list_by_employee'),
    path('events/', event_views.EventList.as_view(), name='event_list_create'),
    path('events/<int:pk>/', event_views.EventDetail.as_view(), name='event_detail_update_destroy'),
    path('inventories/', InventoryList.as_view(), name='inventory_list_create'),
    path('inventories/<int:pk>/', InventoryDetail.as_view(), name='inventory_detail_update_destroy'),
    path('items/', ItemList.as_view(), name='item_list_create'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item_detail_update_destroy'),
]
