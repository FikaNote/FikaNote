from django import forms

class AgendaForm(forms.Form):
    url = forms.URLField()
