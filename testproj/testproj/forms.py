from django import forms


class user_reg_form(forms.Form):
     name = forms.TextInput(attrs={'class':'input'})

