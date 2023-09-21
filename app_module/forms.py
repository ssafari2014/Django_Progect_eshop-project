from django import forms


class app_Form(forms.Form):
    my_form = forms.ImageField()
