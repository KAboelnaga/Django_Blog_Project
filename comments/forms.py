from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['CONTENT']
        widgets = {
            'CONTENT': forms.Textarea(attrs={
                'rows': 2,
                'class': 'form-control',
                'placeholder': 'Write your comment...'
            }),
        }
        labels = {
            'CONTENT': ''
        }
