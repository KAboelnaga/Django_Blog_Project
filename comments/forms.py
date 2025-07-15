from django import forms

class CommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        max_length=500,
        label='Write your comment'
    )
