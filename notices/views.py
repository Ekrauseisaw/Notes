from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Note, Content
from .forms import NoteForm, ContentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    """Home page of app"""
    return render(request, 'notices/index.html')


@login_required
def notes(request):
    """All notes"""
    notes = Note.objects.filter(owner=request.user).order_by('date_added')
    context = {'notes': notes}
    return render(request, 'notices/notes.html', context)


@login_required
def note(request, note_id):
    """Show single note and its content"""
    note = Note.objects.get(id=note_id)
    #current user-topic checkout
    if note.owner != request.user:
        raise Http404
    self_content = note.content_set.order_by('-date_added')
    context = {'note': note, 'content': self_content}
    return render(request, 'notices/note.html', context)


@login_required
def new_note(request):
    """Define a new note"""
    if request.method != 'POST':
        # No data, create empty form
        form = NoteForm()
    else:
        # data POST sent, process the data
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.owner = request.user
            new_note.save()
            return HttpResponseRedirect(reverse('notices:notes'))

    context = {'form': form}
    return render(request, 'notices/new_note.html', context)


@login_required
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


@login_required
def edit_content(request, content_id):
    """Editing note"""
    content = Content.objects.get(id=content_id)
    note = content.note

    if note.owner != request.user:
        raise Http404

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
