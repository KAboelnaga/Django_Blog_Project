from django import forms
from .models import Post, Category, Tags
class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tag name'}),
        }

class PostForm(forms.ModelForm):
    tags_input = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter tags like #tag1 #tag2 (space-separated)'
        })
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
        }
