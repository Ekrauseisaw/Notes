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
]