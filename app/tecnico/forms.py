from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrarTec(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'example@example.cl', 'class':'form-control'},),label="Email")
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'form-control'},),label="Contraseña")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'form-control'},),label="Contraseña")

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrarTec, self).save(commit=False)
        if commit:
            user.save()
        return user