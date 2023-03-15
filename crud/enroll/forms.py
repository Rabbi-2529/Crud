from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
             'email':forms.EmailInput(attrs={'class':'form-control'}),
              'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),     
        }

        def clean(Self):
            clean_data=super().clean()
            valname= Self.clean_data['name']
            if len(valname)<4:
                raise forms.ValidationError('Name more than 4')

  