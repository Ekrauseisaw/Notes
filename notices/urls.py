"""Defines URL patterns for notices"""

from django.urls import path
from . import views

app_name = 'notices'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # All notes
    path('notes/', views.notes, name='notes'),


    # Detail page for a single note
    path('notes/<int:note_id>/', views.note, name="note"),

    # Page for adding new notes
    path('new_note/', views.new_note, name="new_note"),

    # Page for adding new content
    path('new_content/<int:note_id>/', views.new_content, name="new_content"),
    #path('new_content/<int:note_id>/', views.delete_content, name="delete_content"),

    # Page for editing content
    path('edit_content/<int:content_id>/', views.edit_content, name='edit_content'),

    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
]