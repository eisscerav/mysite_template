from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    driver = forms.FloatField(label='cuda_driver')
    toolkit = forms.FloatField(label='cuda_toolkit')

