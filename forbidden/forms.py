from django import forms
from .models import ForbiddenWord
from django import forms
from forbidden.models import ForbiddenWord

class ForbiddenWordsForm(forms.ModelForm):
    class Meta:
        model = ForbiddenWord
        fields = ['word']
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter forbidden word'}),
        }
