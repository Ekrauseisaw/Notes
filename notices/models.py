from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    """ Note title. """
    text = models.CharField(max_length=600)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return string model"""
        return self.text


class Content(models.Model):
    """Content of note."""
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # class Meta

    def __str__(self):
        if self.text[50:]:
            return self.text[:50] + "..."
        else:
            return self.text[:50]
