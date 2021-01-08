from django import forms

class ContactForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)
	your_email = forms.EmailField( max_length= 200, min_length=3)
	subject = forms.CharField(max_length = 200)
	message = forms.TextField()