from django import forms

class PayForm(forms.Form):
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField()
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)
    cardtype = forms.CharField()
    number = forms.CharField()
    expire_month = forms.CharField()
    expire_year = forms.CharField()
    cvv2 = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()