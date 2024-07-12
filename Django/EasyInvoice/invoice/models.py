from django.db import models
from customers.models import Customer
from datetime import datetime


class InvoiceID(models.CharField):
    """
    A custom CharField representing an invoice ID, which is a combination of the current date and a counter.
    
    Attributes:
        max_length (int): The maximum length of the invoice ID string.
        null (bool): Whether the field allows null values. In this case, it's set to False to ensure each invoice has a unique ID.
        blank (bool): Whether the field allows empty strings. In this case, it's set to False to ensure each invoice has a valid ID.

    Methods:
        __init__(self, *args, **kwargs):
            Initializes the InvoiceID field with a maximum length of 20 characters and sets the default value.
        
        get_default_value(self):
            Returns the default value for the invoice ID, which is a combination of the current date and a counter.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, max_length=20, null=False, blank=False)
        self.default = self.get_default_value

    def get_default_value(self):
        now = datetime.now().strftime("%Y%m%d")
        counter = models.IntegerField(default=0).get_default_value()
        return f"{now}_{counter:04d}"


# Create your models here.
class Invoice(models.Model):
    invoice_id = InvoiceID(primary_key=True)    
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    date = models.DateField()
    product = models.CharField(max_length=256)