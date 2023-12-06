from rest_framework import serializers
from . import models

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = ['id', 'title', 'content', 'created_at']

    def save(self, **kwargs):
        user_id = self.context['user_id']
        self.instance = models.Note.objects.create(user_id = user_id, **self.validated_data)
        return self.instance