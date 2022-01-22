from django import forms

class NMForm(forms.Form):
    nmodel = forms.CharField(label='Name', max_length=40)

