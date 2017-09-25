from db_file_storage.form_widgets import DBClearableFileInput
from django import forms

from .models import Link


class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
        exclude = []
        widgets = {
            'image': DBClearableFileInput,
        }
