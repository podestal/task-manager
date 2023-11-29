from django.contrib import admin
from task_manager_api.models import Project, Task

admin.site.register(Project)
admin.site.register(Task)