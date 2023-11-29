from django.db import models
from django.conf import settings

class Project(models.Model):

    PROJECT_STATUS_NOT_STARTED = 'n'
    PROJECT_STATUS_IN_PROGRESS = 'p'
    PROJECT_STATUS_COMPLETED = 'c'

    PROJECT_STATUS = [
        (PROJECT_STATUS_NOT_STARTED, 'not started'),
        (PROJECT_STATUS_NOT_STARTED, 'in progress'),
        (PROJECT_STATUS_COMPLETED, 'completed')
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=PROJECT_STATUS, default=PROJECT_STATUS_NOT_STARTED)

class Task(models.Model):

    TASK_STATUS_NOT_STARTED = 'n'
    TASK_STATUS_IN_PROGRESS = 'p'
    TASK_STATUS_IN_REVISION = 'r'
    TASK_STATUS_COMPLETED = 'c'

    TASK_STATUS = [
        (TASK_STATUS_NOT_STARTED, 'not started'),
        (TASK_STATUS_IN_PROGRESS, 'in progress'),
        (TASK_STATUS_IN_REVISION, 'in revision'),
        (TASK_STATUS_COMPLETED, 'completed'),
    ]

    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=TASK_STATUS, default=TASK_STATUS_NOT_STARTED)


