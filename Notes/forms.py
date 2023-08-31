from django.forms import ModelForm
from .models import sampleNote

class noteForm(ModelForm):
    class Meta:
        model = sampleNote
        fields = ['title', 'description']