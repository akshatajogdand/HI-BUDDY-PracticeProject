from django import forms
from .models import *

# ================================ Employee Form =====================================================

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            'dob': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
            'name' : forms.TextInput(attrs={ 'placeholder': 'Enter your Full name', }),
            'address' :forms.Textarea(attrs={'rows':4, 'cols':30}),     
        }