# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
