from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered")
        return email
        

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password2')
        if (password and password_confirmation) and (password != password_confirmation):
            raise forms.ValidationError("Passwords don't match.")
        
        return cleaned_data
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')
    password = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder':'Enter your password',
        'autocomplete': 'current-password',
        'required': 'required',
        'autofocus': 'autofocus'
    }))