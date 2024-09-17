from django import forms
from .models import single_contact

class contact_form(forms.ModelForm):
    class Meta:
        model = single_contact
        fields = ['first_name', 'last_name', 'email', 'phone_number','address']
        