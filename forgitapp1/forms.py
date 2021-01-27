from django import forms
from .models import RegData,LogData

class RegForm(forms.Form):
    f_name=forms.CharField(
        label="Enter Your First_Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'first_name'
            }
        )
    )
    l_name=forms.CharField(
        label="Enter Your Last_Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'last_name'
            }
        )
    )
    uname=forms.CharField(
        label="Enter Your Username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'username'
            }
        )
    )
    password=forms.CharField(
        label="Enter Your password",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'password'
            }
        )
    )

class LogForm(forms.Form):
    uname=forms.CharField(
        label="Enter Your Username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'username'
            }
        )
    )
    password=forms.CharField(
        label="Enter Your password",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'password'
            }
        )
    )