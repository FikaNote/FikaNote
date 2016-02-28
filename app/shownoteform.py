from django import forms


class ShownoteForm(forms.Form):
    title = forms.CharField()
    agenda = forms.CharField(widget=forms.Textarea)
    person = forms.CharField()
