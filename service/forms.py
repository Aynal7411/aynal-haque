from django import forms
from .models import ClientContact

class ClientContactForm(forms.ModelForm):
    class Meta:
        model = ClientContact
        fields = ['title', 'name', 'email', 'phone', 'message', 'urgent', ]
        INPUT_CLASS = (
         "w-full px-4 py-3 border rounded-lg "
        "focus:ring-2 focus:ring-blue-500"
)
        widgets = {
            'title': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'write your subject here...'}),
            'name': forms.TextInput(attrs={'class':  INPUT_CLASS, 'placeholder': 'write your name here...'}),
            'email': forms.EmailInput(attrs={'class':  INPUT_CLASS, 'placeholder': 'write your email here...'}),
            'phone': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'write your phone number here...'}),
                  
            'message': forms.Textarea(attrs={'class':  "w-full px-4 py-3 border rounded-lg "
                    "focus:ring-2 focus:ring-blue-500","rows": 5, 'placeholder': 'write your message here...'}),

            "urgent": forms.CheckboxInput(attrs={'class': "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 "
                    "focus:ring-2"}),        
                     
        }


    def clean_email(self):

      email = self.cleaned_data.get("email")


      if email:

        blocked_domains = [
            "spam.com",
            "fake.com",
        ]

        domain = email.split("@")[-1]


        if domain in blocked_domains:

            raise forms.ValidationError(
                "This email domain is not allowed."
            )


      return email
    
    def clean_message(self):

      message = self.cleaned_data.get(
        "message"
    )

      if message:
        message = message.strip()

        if len(message) < 20:

         raise forms.ValidationError(
            "Message must contain at least 20 characters."
        )


      if len(message) > 2000:

        raise forms.ValidationError(
            "Message is too long."
        )


      return message
    
    def clean_name(self):

      name = self.cleaned_data.get(
        "name"
    )

      if name:
        name = name.strip()
        if len(name) < 3:

         raise forms.ValidationError(
            "Name is too short."
        )


      return name