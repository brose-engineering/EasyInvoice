from django.db import models
from customers.models import Customer
from datetime import datetime
from django.db.models import Max


# Create your models here.
class Invoice(models.Model):
    invoice_id = models.CharField(max_length=20)

    @classmethod
    def get_next_invoice_id(cls):
        now = datetime.now().strftime("%Y%m%d")
        max_id = cls.objects.aggregate(Max('invoice_id'))['invoice_id__max']
        
        if max_id and str(max_id).startswith(now + '_'):
            return f"{now}_{int(str(max_id)[-4:]) + 1:04d}"
        else:
            return f"{now}_0001"
    """
    The Invoice class defines a table in the database to store invoices.
    """
    # A unique identifier for each invoice, using the classmethod above to generate it.
    invoice_id = models.CharField(max_length=20, primary_key=True, default=lambda: Invoice.get_next_invoice_id())
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