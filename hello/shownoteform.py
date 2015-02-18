from django.utils.translation import gettext_lazy as _
from django import forms

class ShownoteForm(forms.Form):
    title = forms.CharField()
    agenda = forms.CharField()
    person = forms.CharField()
