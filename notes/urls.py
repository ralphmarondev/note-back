from django.urls import path

from .views import *

urlpatterns = [
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/create/', NewNoteView.as_view(), name='new-note')
]
