# forms.py

from django import forms
from .models import Customer

class NewCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name', 'last_name', 'company_name', 'street', 
            'zip_code', 'city', 'email', 'phone', 'mobile'
        ]
        labels = {
            'first_name': "Vorname",
            'last_name': "Nachname",
            'company_name': "Firma",
            'street': "Straße",
            'zip_code': "PLZ",
            'city': "Stadt",
            'email': "E-Mail",
            'phone': "Telefon",
            'mobile': "Mobil",
        }
