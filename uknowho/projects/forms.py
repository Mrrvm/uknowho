from .models import Profile
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()
    email = forms.CharField()

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password']