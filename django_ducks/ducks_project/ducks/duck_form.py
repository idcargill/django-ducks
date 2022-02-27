from django import forms

class DuckForm(forms.Form):
  duck_name = forms.CharField(label='Duck Name', max_length=50)
