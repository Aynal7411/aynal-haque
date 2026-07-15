from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import  UserProfile



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email Address",
        help_text="Enter a valid email address.",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter your email",
                "autocomplete": "email",
            }
        ),
    )

    username = forms.CharField(
        max_length=150,
        label="Username",
        help_text="Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Choose a username",
                "autocomplete": "username",
            }
        ),
    )

    password1 = forms.CharField(
        label="Password",
        help_text="Minimum 8 characters with letters and numbers.",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Create a strong password",
                "autocomplete": "new-password",
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Confirm your password",
                "autocomplete": "new-password",
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"]

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "This email address is already registered."
            )

        return email

    def clean_password1(self):
        password = self.cleaned_data["password1"]

        if len(password) < 8:
            raise forms.ValidationError(
                "Password must be at least 8 characters long."
            )

        if not any(c.isalpha() for c in password):
            raise forms.ValidationError(
                "Password must contain at least one letter."
            )

        if not any(c.isdigit() for c in password):
            raise forms.ValidationError(
                "Password must contain at least one number."
            )

        return password


class UserProfileForm(forms.ModelForm):
    """Form for editing user profile information"""
    first_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'phone', 'location', 'linkedin', 'github', 'twitter', 'portfolio']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tell us about yourself'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 (555) 000-0000'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City, Country'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/yourprofile'}),
            'github': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/yourprofile'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://twitter.com/yourprofile'}),
            'portfolio': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://yourportfolio.com'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
            user = profile.user
            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.email = self.cleaned_data.get('email')
            user.save()
        return profile


class UserPasswordChangeForm(forms.Form):
    """Form for changing user password"""
    old_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
        help_text='Must be at least 8 characters with letters and numbers.'
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Your old password is incorrect.')
        return old_password

    def clean_new_password1(self):
        new_password = self.cleaned_data.get('new_password1')
        if len(new_password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        if not any(char.isdigit() for char in new_password):
            raise forms.ValidationError('Password must contain at least one number.')
        if not any(char.isalpha() for char in new_password):
            raise forms.ValidationError('Password must contain at least one letter.')
        return new_password

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned_data

