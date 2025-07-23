from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    Birth_Date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Student
        exclude = ['user']