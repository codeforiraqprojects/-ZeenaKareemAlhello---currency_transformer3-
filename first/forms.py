from django import forms
from first.models import signin

class signin2(forms.ModelForm):
    class Meta:
       model = signin
       fields = ['fullname','email']
       labels = {
           'fullname': 'Enter Fullname',
           'email': 'Enter Your Email',


        }




