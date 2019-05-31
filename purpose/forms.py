from django import forms
from .models import *
class AddList(forms.ModelForm):
    class Meta:
        model=list
        fields=['name']

class UpdateList(forms.ModelForm):
    class Meta:
        model=list
        fields=['name','section']
