from rest_framework import serializers
from .models import Note
class NoteSerializer(serializers.ModelSerializer):
    #image = serializers.SerializerMethodField()
    class Meta:
        model = Note
        fields = ('id', 'title', 'body', 'created_at','image')
