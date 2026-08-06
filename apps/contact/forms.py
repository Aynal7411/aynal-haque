from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150, required=False)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
