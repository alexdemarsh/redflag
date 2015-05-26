from django import forms


class UploadFileForm(forms.Form):
	name = forms.CharField(max_length=100)
	docfile = forms.FileField(label='csv data', help_text='max 42 mb')