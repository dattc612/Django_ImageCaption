from django import forms

class ImageForms(forms.Form):
	img = forms.ImageField(label=' ')


class SendMail(forms.Form):
	first_name = forms.CharField(max_length = 30)
	last_name = forms.CharField(max_length =30 )
	message = forms.CharField(max_length = 50)
	to_email = forms.CharField(max_length=100)