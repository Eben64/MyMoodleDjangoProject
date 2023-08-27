from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Project, User, Submission


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    nom = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    prenom = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    date_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    numero = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username','password1', 'password2', 'nom', 'prenom', 'date_birth', 'numero', 'is_admin', 'is_teacher', 'is_student')

class EditUserForm(forms.ModelForm):
    nom = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    prenom = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        )
    date_birth = forms.DateField(
            widget=forms.DateInput(
                attrs={
                    "class": "form-control"
                }
            )
        )
    numero = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        )
    class Meta:
            model = User
            fields = ['username', 'nom', 'prenom', 'numero', 'is_admin', 'is_teacher', 'is_student']

class DeleteUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [] 

class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [ 'submission_deadline', 'uploaded_by', 'file']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['submission_file']