from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from task_manager_api.models import Project, Task
from task_manager_api.serializers import ProjectSerializer, TaskSerializer, CreateProjectSeralizer

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Project.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateProjectSeralizer
        return ProjectSerializer
    
    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
        

class TaskViewSet(ModelViewSet):

    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.filter(project_id = self.kwargs['project_pk'])
    
    def get_serializer_context(self):
        return {'project_id': self.kwargs['project_pk']}
    
