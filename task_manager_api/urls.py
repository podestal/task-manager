from rest_framework_nested import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('projects', views.ProjectViewSet, basename='projects')
router.register('tasks', views.TaskViewSet)

urlpatterns = router.urls