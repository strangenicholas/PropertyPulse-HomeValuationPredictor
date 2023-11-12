from django import forms
from .models import HouseData

class HouseDataForm(forms.ModelForm):
    class Meta:
        model = HouseData
        fields = '__all__'