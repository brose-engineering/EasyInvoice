from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    company_name = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5)  # Use CharField to allow leading zeros
    city = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=32, blank=True)  # Use CharField to store phone numbers
    mobile = models.CharField(max_length=32, blank=True)  # Use CharField to store mobile numbers

    def __str__(self):
        return f'{self.customer_id} - {self.company_name}'
