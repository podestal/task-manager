from rest_framework import serializers
from task_manager_api.models import Project, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'created_at', 'status']

    def save(self, **kwargs):
        project_id = self.context['project_id']
        self.instance = Task.objects.create(project_id = project_id, **self.validated_data)
        return self.instance
    

class ProjectSerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created_at', 'last_updated' ,'status', 'tasks']

class CreateProjectSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'slug', 'description']

    def save(self, **kwargs):
        user_id = self.context['user_id']
        self.instance = Project.objects.create(user_id = user_id, **self.validated_data)
        return self.instance

