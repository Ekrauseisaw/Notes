from django.shortcuts import render
from .models import Note

# Create your views here.


def index(request):
    """Home page of app"""
    return render(request, 'notices/index.html')


def notes(request):
    """All notes"""
    notes = Note.objects.order_by('date_added')
    context = {'notes': notes}
    return render(request, 'notices/notes.html', context)


def note(request, note_id):
    """Show single note and its content"""
    note = Note.objects.get(id=note_id)
    self_content = note.content_set.order_by('-date_added')
    context = {'note': note, 'content': self_content}
    return render(request, 'notices/note.html', context)
