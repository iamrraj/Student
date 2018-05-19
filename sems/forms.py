from django import forms
from .models import Upload
from django.contrib.auth.models import User

class UploadFormFile(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('name', 'file', 'course', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=128, widget = forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget = forms.PasswordInput())
    password2 = forms.CharField(widget = forms.PasswordInput())


    def clean_username(self):
        try:
            User.objects.get(username__iexact=self.username)
            raise forms.ValidationError('User already exists')
        except User.DoesNotExist:
            return self.username


    def clean_password(self):
        pw1 = self.cleaned_data.get('password1')
        pw2 = self.cleaned_data.get('password2')

        if pw1 and pw2 and pw1 == pw2:
            return pw1
        raise forms.ValidationError("Password doesn't match")
