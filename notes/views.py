from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers

class NotesViewSet(ModelViewSet):

    serializer_class = serializers.NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return models.Note.objects.filter(user_id = user_id)
    
    def get_serializer_context(self):
        return {'user_id' : self.request.user.id}
