from django import forms
from django.forms import ModelForm
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


# Create a SHACL Pattern Form
class SHACLPatternForm(ModelForm):
    class Meta:
        model = SHACLPattern
        fields = '__all__'

        widgets = {
            'pattern': forms.Select(attrs={
                'maxlength': 10,
                'class': 'form-control details text-secondary',
                }),            
            'code': forms.TextInput(attrs={
                'maxlength': 10,
                'class': 'form-control details text-secondary',
                }),
            'description': forms.Textarea(attrs={
                'class': 'form-control details text-secondary',
                'row': 4,
                }),
            'shacl_pattern': forms.Textarea(attrs={
                'class': 'form-control details text-secondary',
                'row': 10,
                }), 
        }
