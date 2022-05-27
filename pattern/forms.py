from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import ClassPattern, SHACLPattern


# Create a Class Pattern Form
class ClassPatternForm(ModelForm):
    class Meta:
        model = ClassPattern
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'maxlength': 50,
                'class': 'form-control details text-secondary',
                }),
            'description': forms.Textarea(attrs={
                'class': 'form-control details text-secondary',
                'row': 4,
                }),
        }
