from django import forms
from django.forms import ModelForm
from .models import PatternInstance


# Create a Pattern Instance Form
class PatternInstanceForm(ModelForm):
    class Meta:
        model = PatternInstance
        fields = '__all__'

        widgets = {
            'shacl_pattern': forms.Select(attrs={
                'class': 'form-select details text-dark',
                }),  
            'name': forms.TextInput(attrs={
                'maxlength': 150,
                'class': 'form-control details text-dark',
                }),
            'description': forms.Textarea(attrs={
                'class': 'form-control details text-dark',
                'rows': 4,
                }),
            'creator': forms.TextInput(attrs={
                'maxlength': 100,
                'class': 'form-control details text-dark',
                }),
            'shacl_shapes': forms.Textarea(attrs={
                'class': 'form-control code text-dark',
                'rows': 10,
                'wrap': 'off',
                }),
        }
