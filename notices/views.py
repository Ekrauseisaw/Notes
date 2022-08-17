from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Note, Content
from .forms import NoteForm, ContentForm

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


def new_note(request):
    """Define a new note"""
    if request.method != 'POST':
        # No data, create empty form
        form = NoteForm()
    else:
        # data POST sent, process the data
        form = NoteForm(request.POST)
        if form.is_valid():
            #new_note = form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse('notices:notes'))

    context = {'form': form}
    return render(request, 'notices/new_note.html', context)


def new_content(request, note_id):
    """Adding new content for particular note"""
    note = Note.objects.get(id=note_id)

    if request.method != 'POST':
        # No data, create empty form
        form = ContentForm()
    else:
        # data POST sent, process the data
        form = ContentForm(data=request.POST)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.note = note
            new_content.save()
            return HttpResponseRedirect(reverse('notices:note',
                                                args=[note_id]))

    context = {'note': note, 'form': form}
    return render(request, 'notices/new_content.html', context)


def edit_content(request, content_id):
    """Editing note"""
    content = Content.objects.get(id=content_id)
    note = content.note

    if request.method != 'POST':
        form = ContentForm(instance=content)
    else:
        form = ContentForm(instance=content, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notices:note',
                                                args=[note.id]))

    context = {'content': content, 'note': note, 'form': form}
    return render(request, 'notices/edit_content.html', context)
