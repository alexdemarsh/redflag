from django import forms
import datetime

class UploadFileForm(forms.Form):
	name = forms.CharField(max_length=50)
	description = forms.CharField(max_length=500)
	file = forms.FileField()
	# created = forms.DateField(initial=datetime.utcnow)
	owner = forms.BooleanField(initial=True)

