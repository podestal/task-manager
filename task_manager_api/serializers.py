from rest_framework import serializers
from task_manager_api.models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created_at', 'last_updated' ,'status']

class CreateProjectSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'slug', 'description']

    def save(self, **kwargs):
        user_id = self.context['user_id']
        self.instance = Project.objects.create(user_id = user_id, **self.validated_data)
        return self.instance

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
