from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 255)
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not username and not password:
            raise forms.ValidationError('Add username and password')


class AddClient(forms.ModelForm):
    CHOICES=[
        (1,'Yes'),
        (0,'No')
    ]

    active = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Client
        fields = ('name', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'country', 'active')
