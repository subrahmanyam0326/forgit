from django import forms
from .models import RegData,LogData

class RegForm(forms.Form):
    class Meta:
        model=RegData
        fields="__all__"
class LogForm(forms.Form):
    class Meta:
        model=LogData
        fields="__all__"