from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    company_name = models.CharField(max_length=64, blank=True, null=True)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.customer_id} - {self.name}'
