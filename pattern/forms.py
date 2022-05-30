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
                'class': 'form-control details text-dark',
                }),
            'description': forms.Textarea(attrs={
                'class': 'form-control details text-dark',
                'row': 4,
                }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control details text-dark',
                }),
        }


# Create a SHACL Pattern Form
class SHACLPatternForm(ModelForm):
    class Meta:
        model = SHACLPattern
        fields = '__all__'

        widgets = {
            'pattern_class': forms.Select(attrs={
                'class': 'form-select details text-dark',
                }),  
			'order': forms.NumberInput(attrs={
                'class': 'form-control details text-dark',
                }),          
            'code': forms.TextInput(attrs={
                'maxlength': 10,
                'class': 'form-control details text-dark',
                }),
            'description': forms.Textarea(attrs={
                'class': 'form-control details text-dark',
                'row': 4,
                }),
            'shacl_pattern': forms.Textarea(attrs={
                'class': 'form-control code text-dark',
                'row': 10,
                'wrap': 'off',
                }), 
        }
