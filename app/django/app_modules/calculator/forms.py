from django import forms

class TaxForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    tax_code = forms.IntegerField(label='Tax Code', min_value=1, max_value=3, required=True)
    amount = forms.IntegerField(label='Amount', min_value=1, required=True)
