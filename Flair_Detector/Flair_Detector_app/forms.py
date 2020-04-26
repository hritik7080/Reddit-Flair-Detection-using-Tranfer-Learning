from django import forms


class get_title(forms.Form):
    link = forms.CharField(max_length=2000)