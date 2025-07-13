from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note
from .serializers import NoteSerializer


class NewNoteView(APIView):
    def post(self, request):
        data = request.data
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            note = serializer.save()
            note.save()
            return Response(
                data={'note': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class NoteListView(APIView):
    def get(self, request):
        notes = Note.objects.filter(is_deleted=False)
        serializer = NoteSerializer(notes, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
