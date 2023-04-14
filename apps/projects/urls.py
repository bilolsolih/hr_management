from django.urls import path
from .api_endpoints.project import views as project_views
from .api_endpoints.team import views as team_views

app_name = 'projects'

urlpatterns = [
    path('teams/', team_views.TeamList.as_view(), name='position_list_create'),
    path('teams/<int:pk>/', team_views.TeamDetail.as_view(), name='position_detail_update_destroy'),
    path('projects/', project_views.ProjectList.as_view(), name='employee_list_create'),
    path('projects/<int:pk>/', project_views.ProjectDetail.as_view(), name='employee_detail_update_destroy'),
]
