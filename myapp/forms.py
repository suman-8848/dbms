from .models import customer
from django import forms


class Form(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = customer
        fields = ['Name', 'Email', 'phone_number','costID',
                  'state', 'postal_code', 'username', 'password']
