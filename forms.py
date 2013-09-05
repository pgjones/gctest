from django import forms

from gctest.models import App, Build, Developer

class AppForm(forms.ModelForm):
    class Meta:
        model = App

class BuildForm(forms.ModelForm):
    class Meta:
        model = Build

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
