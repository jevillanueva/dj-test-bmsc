"""
Forms for the country a
"""
from django import forms
from .models import Country, City

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['codigo', 'descripcion', 'is_active']

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['codigo', 'descripcion', 'is_active']