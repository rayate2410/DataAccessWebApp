from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import TestCase



class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
   
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            print user
            user.save()
            
        return user
    
    

class AddTestCase(forms.ModelForm):
    
    class Meta:
        model = TestCase
        