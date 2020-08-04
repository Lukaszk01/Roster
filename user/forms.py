from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=''))
    full_name = forms.CharField()
    phone_number = forms.IntegerField()
    gender = forms.fields.ChoiceField(
        choices = (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        ),
        required=True,
        widget=forms.widgets.Select
    )
    position = forms.fields.ChoiceField(
        choices = (
            ('R', 'Runner'),
            ('S', 'Server'),
            ('Rsp', 'Reception'),
            ('B', 'Bartender'),
            ('O', 'Other'),

        ),
        required=True,
        widget=forms.widgets.Select
    )
    employment = forms.fields.ChoiceField(
        choices = (
            ('F', 'Full-Time'),
            ('P', 'Part-Time'),
            ('O', 'Other'),


        ),
        required=True,
        widget=forms.widgets.Select
    )

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'password1', 'password2', 'phone_number', 'birth_date', 'gender', 'position', 'employment']


class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()
  full_name = forms.CharField()
  gender = forms.fields.ChoiceField(
        choices = (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        ),
        required=True,
        widget=forms.widgets.Select
    )

  class Meta:
      model = User
      fields = ['username', 'email', 'gender', 'full_name']





