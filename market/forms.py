from django import forms
from market.models import (
   House
)

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'

    def cleanHouseName(self):
        return self.cleaned_data['houseName'].strip()

