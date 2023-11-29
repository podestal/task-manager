from rest_framework_nested import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('projects', views.ProjectViewSet, basename='projects')

tasks_router = routers.NestedDefaultRouter(router, 'projects', lookup='project')
tasks_router.register('tasks', views.TaskViewSet, basename='tasks')

urlpatterns = router.urls + tasks_router.urls