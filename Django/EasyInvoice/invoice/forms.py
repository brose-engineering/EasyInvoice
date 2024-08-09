# forms.py to create a form for a new customer

from django import forms
from .models import Invoice
from datetime import datetime

class DateTimeLocalInput(forms.DateInput):
    def __init__(self, attrs=None, format='%Y-%m-%d'):
        super().__init__(attrs)
        self.input_type = 'date'

class newInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_id', 'customer', 'date', 'product']
        labels = {
            'invoice_id': 'Rechnungsnummer',
            'customer': 'Kunde',
            'date': 'Datum',
            'product': 'Produkt',
            }
        widgets = {
            # Map the 'date' field to use DateInput instead of the standard text input
            'date': DateTimeLocalInput,
        }

    date = forms.DateField(widget=DateTimeLocalInput, initial=datetime.now().strftime('%Y-%m-%d'))
