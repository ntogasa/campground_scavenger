from django import forms

class ContactForm(forms.Form):
    """Specifies the input fields and objects for the contact form"""
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)