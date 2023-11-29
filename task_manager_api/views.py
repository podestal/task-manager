from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from task_manager_api.models import Project, Task
from task_manager_api.serializers import ProjectSerializer, TaskSerializer

@api_view()
def sampleView(request):
    return Response('ok')

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer