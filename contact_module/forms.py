from django.forms import ModelForm
from .models import ContactUsModel
from django import forms


class contactUsForms(ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ['fullname', 'email', 'title', 'message']

        labels = {
            'fullname': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'title': 'عنوان',
            'message': 'متن پیام',
        }
        error_messages = {
            'fullname': {
                'required': 'نام و نام خانوادگی خود را وارد کنید دوست عزیز'
            },
            'email': {
                'required': 'لطفا ایمیل خود را وارد کنیددوست عزیز'
            },
            'title': {
                'required': 'عنوان پیام خود را وارد کنیددوست عزیز'
            },
            'message': {
                'required': 'لطفا متن پیام خود را وارد کنید دوست عزیز'
            },
        }

        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'متن پیام',
                'rows': '8',
                'id': 'message'
            }),
        }
