from django import forms
import re


class EmailForm(forms.Form):
    subject = forms.CharField(label='Enter subject')
    sender = forms.EmailField(label='Enter email to send')
    message = forms.CharField()

    def clean_sender(self):
        sender = self.cleaned_data['sender']
        pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
        if not re.match(pattern, sender):
            raise forms.ValidationError('You must enter a valid email address')
        return sender
