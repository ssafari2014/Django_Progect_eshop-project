from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class registerForm(forms.Form):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput())
    password = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput())
    repeat_password = forms.CharField(label='تکرار کلمه عبور', widget=forms.PasswordInput())

    def clean_repeat_password(self):
        user_pass = self.cleaned_data.get('password')
        repeat_pass = self.cleaned_data.get('repeat_password')
        if user_pass == repeat_pass:
            return repeat_pass
        else:
            raise ValidationError(message='کلمه عبور و تکرار کلمه عبور یکسان نیست !!!')


class loginForm(forms.Form):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput())
    password = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput())


class ForgotForm(forms.Form):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput())


class ResetForm(forms.Form):
    password = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput())
    repeat_password = forms.CharField(label='تکرار کلمه عبور', widget=forms.PasswordInput())
