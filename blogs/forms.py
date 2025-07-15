from django import forms
from .models import Post, Category, ForbiddenWord

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['id','title', 'content', 'category','author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),

        }
    def clean_content(self):
        content = self.cleaned_data.get('content')
        forbidden_words = ForbiddenWord.objects.values_list('word', flat=True)

        for word in forbidden_words:
            if word.lower() in content.lower():
                raise forms.ValidationError(f"this word '{word}' is not allowed in the content.")
        return content


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
        }