from django import forms
from models import TestCase



class AddTestCase(forms.ModelForm):
    
    class Meta:
        model = TestCase
        