from django.urls import path

from .api_endpoints.employee import views as employee_views
from .api_endpoints.employee.list.views import EmployeeList
from .api_endpoints.employee.retrieve.views import EmployeeRetrieve
from .api_endpoints.employee.delete.views import EmployeeDelete
from .api_endpoints.position import views as position_views

app_name = 'employees'

urlpatterns = [
    path('positions/', position_views.PositionList.as_view(), name='position_list_create'),
    path('positions/<int:pk>/', position_views.PositionDetail.as_view(), name='position_detail_update_destroy'),
    # path('employees/', employee_views.EmployeeList.as_view(), name='employee_list_create'),
    # path('employees/<int:pk>/', employee_views.EmployeeDetail.as_view(), name='employee_detail_update_destroy'),
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/detail/<int:pk>/', EmployeeRetrieve.as_view(), name='employee_detail'),
    path('employees/delete/<int:pk>/', EmployeeDelete.as_view(), name='employee_delete'),
]
