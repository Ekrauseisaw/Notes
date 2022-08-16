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
]