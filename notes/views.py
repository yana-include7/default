from django.shortcuts import render
from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import action
from .models import Note
from .serializers import NoteSerializer
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer

    @action(methods=['post'], detail=True)
    def upload_docs(request):
        print("данные",request.data)
        try:
            file = request.data['file']
        except KeyError:
            print('Request has no resource file attached')
        product = Note.objects.create(image=file)