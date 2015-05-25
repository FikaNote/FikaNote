from django import forms

class ShownoteForm(forms.Form):
    title = forms.CharField()
    agenda = forms.CharField()
    person = forms.CharField()
