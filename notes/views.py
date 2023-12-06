from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers

class NotesViewSet(ModelViewSet):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
