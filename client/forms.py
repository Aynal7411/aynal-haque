from django import forms
from .models import BusinessUser

class BusinessRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = BusinessUser
        fields = [
            'country', 'trade_role', 'email',
            'password', 'confirm_password',
            'company_name', 'full_name',
            'phone', 'agree_terms'
        ]
        widgets = {
            'agree_terms': forms.CheckboxInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
