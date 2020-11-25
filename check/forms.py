from django import forms
from check.models import Check


class CheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['time', 'cafeteria', 'menu']

        widgets = {
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            'cafeteria': forms.TextInput(attrs={'class': 'form-control'}),
            'menu': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
