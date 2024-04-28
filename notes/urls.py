from django.urls import path
from .views import (
    NoteListView,
    NoteDetailView,
    NoteCreateView,
    NoteEditView,
    NoteDeleteView,
    TagListView,
    TagCreateView,
    TagEditView,
    TagDeleteView,
    toggle_note_done,
)

app_name = 'notes'

urlpatterns = [
    # Нотатки
    path('', NoteListView.as_view(), name='note_list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('notes/create/', NoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/edit/', NoteEditView.as_view(), name='note_edit'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
    path('toggle_done/<int:pk>/', toggle_note_done, name='toggle_done'),
    # Теги
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tags/create/', TagCreateView.as_view(), name='tag_create'),
    path('tags/<int:pk>/edit/', TagEditView.as_view(), name='tag_edit'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag_delete'),
]