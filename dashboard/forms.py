from django import forms
from . models import Smart_Meter_Data


class Smart_Meter_DataForm(forms.ModelForm):
    class Meta:
        model = Smart_Meter_Data
        fields = ['meter_id', 'location', 'region']
