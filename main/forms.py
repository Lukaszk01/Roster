from django import forms

from .models import Customer
from django.forms import ModelForm

class HomeForm(forms.Form):
        post = forms.CharField()


class InputForm(forms.Form): 
    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput()) 

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'