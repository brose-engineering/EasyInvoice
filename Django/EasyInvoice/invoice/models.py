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
    """
    The Invoice class defines a table in the database to store invoices.
    """
    # A unique identifier for each invoice, serving as the primary key.
    invoice_id = InvoiceID(primary_key=True)    
    """
    This attribute uniquely identifies each invoice and is used 
    as the primary key for this model. It's an instance of InvoiceID, 
    which could be a custom class or a built-in Python type like int or str.
    """
    # The customer who made the purchase, linked to the Customer model via a foreign key.
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    """
    This attribute links each invoice to its corresponding customer. 
    It's a foreign key that references the Customer model.
    If the customer record is deleted, this association will be set to null (DO_NOTHING).
    """
    # The date when the invoice was created or issued.
    date = models.DateField()
    """
    This attribute represents the date when the invoice was created 
    or issued. It's a standard DateField, which expects dates in YYYY-MM-DD format.
    """
    # A brief description of the product(s) being invoiced.
    product = models.CharField(max_length=256)
    """
    This attribute provides a short summary or description of the product(s) 
    being invoiced. The maximum length is 256 characters, suitable for short descriptions.
    """
    def __str__(self):
        return f'Rechnung {self.invoice_id} vom {self.date} für Kunde {self.customer.first_name} {self.customer.last_name}'